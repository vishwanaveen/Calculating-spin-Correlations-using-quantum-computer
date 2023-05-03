from qiskit import QuantumCircuit, execute, Aer
import numpy as np

# Create the |W> state
def w_state(qc, qubits):
    n = len(qubits)
    qc.h(qubits[0])
    for i in range(1, n):
        qc.cx(qubits[0], qubits[i])
    return qc

# Define the circuit to measure <W|(σθ⊗σθ⊗σθ)|W>
def sigma_theta_circuit(theta):
    qubits = range(3)
    qc = QuantumCircuit(len(qubits), len(qubits))
    
    # Create the |W> state
    qc = w_state(qc, qubits)
    
    # Apply the tensor product of sigma_theta operators
    qc.s(qubits[0])
    qc.s(qubits[1])
    qc.s(qubits[2])
    qc.h(qubits)
    qc.cz(qubits[0], qubits[1])
    qc.cz(qubits[1], qubits[2])
    
    # Measure the circuit
    qc.measure(qubits, qubits)
    
    return qc

# Estimate the expectation value of <W|(σθ⊗σθ⊗σθ)|W>
def estimate_sigma_theta(theta):
    qc = sigma_theta_circuit(theta)
    shots = 1024
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=shots)
    counts = job.result().get_counts(qc)
    numerator = counts.get('000', 0) + counts.get('011', 0) + counts.get('101', 0) + counts.get('110', 0)
    denominator = counts.get('001', 0) + counts.get('010', 0) + counts.get('100', 0) + counts.get('111', 0)
    expectation_value = (numerator - denominator) / shots
    return expectation_value

# Main code to loop over theta values and estimate the expectation value
theta_values = np.arange(0, np.pi, np.pi/18)
results = []
for theta in theta_values:
    expectation_value = estimate_sigma_theta(theta)
    results.append(expectation_value)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(theta_values, results)
plt.xlabel('Theta')
plt.ylabel('Expectation value')
plt.show()
