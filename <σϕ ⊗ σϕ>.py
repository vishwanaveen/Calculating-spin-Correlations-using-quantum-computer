import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Define the states to measure
states = ['00', '11', '01+10', '01-10']

# Define the range of phi values to measure
phi_vals = np.arange(0, 2*np.pi, np.pi/8)

# Define the quantum circuit
qc = QuantumCircuit(2, 1)

for state in states:
    print(f"Expectation values for state {state}:")
    for phi in phi_vals:
        # Prepare the initial state
        if state == '00':
            pass
        elif state == '11':
            qc.x(0)
            qc.x(1)
        elif state == '01+10':
            qc.h(0)
            qc.cx(0,1)
        elif state == '01-10':
            qc.x(0)
            qc.h(1)
            qc.cx(0,1)
        
        # Apply the sigma phi tensor product sigma phi gate
        qc.ry(phi, 0)
        qc.ry(phi, 1)
        qc.measure(0, 0)
        
        # Run the circuit on a quantum simulator
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(qc, backend=simulator, shots=1024).result()
        counts = result.get_counts(qc)
        
        # Calculate the expectation value
        if '0' in counts:
            exp_val = (counts['0']/1024) - 0.5
        else:
            exp_val = -0.5
        
        print(f"Phi = {phi:.2f}, Expectation value = {exp_val:.4f}")
        
        # Reset the quantum circuit for the next measurement
        qc.reset()
