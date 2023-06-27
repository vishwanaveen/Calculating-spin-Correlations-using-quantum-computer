<a name="br1"></a> 

Calculating spin correlations with a IBM

quantum computer

Naveen Vishwakarma

Abstract

In the rapidly growing ﬁeld of quantum computing, which straddles the boundaries of

physics, computer science, and engineering, computations that are impossible for classical

computers to handle are attempted. Quantum computers use quantum bits, or qubits, which

can simultaneously be both 0 and 1. This is in contrast to classical computers, which store

information in binary bits that can either have a value of 0 or 1. This characteristic makes

some calculations tenfold faster on quantum computers than on conventional ones. Quantum

computing has the potential to revolutionize a number of industries, including machine learn-

ing, drug discovery, and optimization. For instance, many of the cryptographic methods used

to safeguard sensitive information could be cracked by quantum computers, and they could

mimic the behavior of intricate molecules to help develop new drugs. The delicate nature of

qubits, which are often perturbed by outside noise and interactions with other qubits, makes

it diﬃcult to develop viable quantum computers. To solve these issues, researchers are in-

vestigating a range of strategies, such as the use of fault-tolerant structures, error-correcting

codes, and new materials and technologies. Despite these obstacles, quantum computing has

advanced quickly in recent years with the creation of processors with numerous qubits and

the demonstration of quantum supremacy, in which a quantum computer successfully com-

pletes a task that is impossible for classical computers. The impact of quantum computing is

anticipated to be signiﬁcant as the technology develops.

1\. Introduction

The use of quantum-mechanical phenomena, such as superposition, interference, and entangle-

ment, to carry out calculations that are impossible for classical computers is known as quantum

computation. In order to tackle particular problems more quickly than classical algorithms, quan-

tum algorithms are specialized algorithms created to run on quantum computers. They take

advantage of the distinctive properties of quantum mechanics. Cryptography, optimization, and

simulation are just a few of the industries that quantum computing has the potential to revolu-

tionize. For instance, the quantum algorithm Shor’s algorithm is capable of eﬃciently factoring

enormous numbers, a task that is impossible for classical computers to solve. Given that many

cryptographic protocols rely on the diﬃculty of factoring large numbers, this has important im-

plications for cryptography. Database searches can be carried out much more quickly than using

classical algorithms by using other quantum techniques, such as Grover’s algorithm.

In this, we go over more experiments that physicists might ﬁnd interesting. Despite not being

a spin-1/2 particle, the IBM qubit is a two-state system, so the same mathematics applies to both.

A qubit can represent any spin direction by using the Bloch sphere. We simulate the correlation

of spins in systems of two and three particles using quantum circuits. We show the singlet state’s

rotational invariance, the triplet states’ intriguing characteristics, and the startling characteristics

of a tripartite state. These studies support intellectual and visual comprehension of total spin

and spin components. Overall, this report aims to provide a comprehensive understanding of the

intersection between quantum computing and spin correlation.

1



<a name="br2"></a> 

2

ENTANGLEMENT

2

2\. Entanglement

Entanglement is an important concept in quantum physics that describes the correlation be-

tween two or more quantum states. When two or more quantum systems become entangled, their

properties become connected, and measurements on one system can impact the properties of the

other system(s), even if they are far apart. This correlation between the systems is non-local and

cannot be explained by classical physics.

Entanglement emerges from the quantum physics superposition principle, which permits par-

ticles to exist in several states at the same time. When two or more particles become entangled,

their states become entangled as well, resulting in a composite state that cannot be described as

a product of the individual states.

3\. Spin

In quantum physics, spin is a fundamental feature of elementary particles. It’s a form of intrinsic

angular momentum that a particle has even when it’s not moving. In three-dimensional space, spin

is represented as a vector, and its magnitude is quantized in integer or half-integer values in units

of Planck’s constant divided by 2π

Many areas of physics rely on spin, including quantum mechanics, particle physics, and con-

densed matter physics. Spin is employed in quantum mechanics to characterise a particle’s angular

momentum, and it is important in the idea of quantum entanglement. Spin is used in particle

physics to categorise particles into categories such as bosons and fermions, which have diﬀering

spin properties. In the case of condensed matter physics, spin is used to describe the magnetic

properties of materials and the behavior of electrons in solids.

4\. Spin Correlations

One of the most interesting features of spin is its relationship with quantum entanglement.

When two particles are entangled, their spins become correlated, even if the particles are separated

by large distances. This property is known as spin correlation or spin entanglement, and it is the

basis for many proposed applications of quantum computing, such as quantum cryptography and

quantum teleportation.

5\. Qubit

Qubits are the building blocks of quantum computers and quantum communication systems.A

qubit, a basic unit of quantum information, is represented geometrically in the Bloch sphere. Each

point on the Bloch sphere corresponds to a diﬀerent quantum state of the qubit.The computational

basis of a single qubit consists of the states |0〉 and |1〉.

Bloch vector: ⃗n = sin θ cos ϕ⃗i , sin θ sin ϕ ⃗j + cos θ⃗k.

wave function:|ψ> = cos(θ/2)|0> + e<sup>iϕ</sup> sin(θ/2)|1>

Figure 1. Bloch Sphere



<a name="br3"></a> 

6

KRONECKER PRODUCT

3

where θ varies from 0 to π ,0〉 and |1〉 are eigenvectors of Pauli spin matrix σ<sub>z</sub> .

The measurement of spin in an arbitrary direction n is associated with the operator σ.n.

where σ = σ ⃗i + σ ⃗j + σ ⃗k so

x

y

z

ꢀ

ꢁ

n<sub>z</sub>

n<sub>x</sub> + in<sub>y</sub>

n − in

x

−n<sub>z</sub>

y

σ · ⃗n =

6\. Kronecker product

The Kronecker product is obtained by straightforward manipulations and denoted by ⊗

ꢀ

ꢁ

ꢀ

ꢁ

a<sub>z</sub>

a<sub>x</sub> + ia<sub>y</sub>

a − ia

b<sub>z</sub>

b − ib

x

−a<sub>z</sub>

y

x

−b<sub>z</sub>

y

σ.a ⊗ σ.b =

⊗

b<sub>x</sub> + ib<sub>y</sub>









a b

a (b − ib )

(a − ia )b

(a − ia )(b − ib )

z

z

a (b + ib )

z

x

y

x

y

z

x

y

x

y

−a b

(a − ia )(b + ib )

−(a − ia )b



z

x

y

(a + ia )b

z

z

x

y

x

y

x

y

z



σ.a⊗σ.b =





(a + ia )(b − ib )

−a b

−a (b − ib )

x

y

(a + ia )(b + ib )

z

x

y

x

y

z

z

z

x

y

−(a + ia )b

−a (b + ib )

a b

z

x

y

x

y

x

y

z

z

x

y

z

7\. Spin correlation function

The anticipated value of the product of the measurements, where one particle’s spin is measured

in the direction and another particle’s spin is measured in the b direction, the expectation value

of the product of the measurements (neglecting factors of h/2) is σ.a ⊗ σ.b. So, < σ.a ⊗ σ.b > is

called spin correlation function.

8\. Quantum states

A quantum state represents the state of a given quantum system. The state of a quantum

system is described by a wave function, which is a mathematical function that contains all the

information related to the system that can be measured. The wave function can be written using

the Dirac notation as:

X<sup>n</sup>

|ψ⟩ =

c<sub>i</sub>|i⟩

i=1

where |ψ⟩ is the quantum state, c are complex numbers known as probability amplitudes, and |i⟩

i

are the basis states. The basis states form a complete orthonormal basis, which means that any

quantum state can be expressed as a linear combination of basis states with complex coeﬃcients.

The probability of measuring a particular basis state |i⟩ when the system is in the state |ψ⟩ is

given by the absolute value squared of the probability amplitude c , i.e., |c |<sup>2</sup>. The sum of the

i

i

probabilities of measuring all possible basis states is equal to 1.

9\. Bell state

A Bell state, also known as an EPR pair (Einstein-Podolsky-Rosen pair) after the names of

the scientists who ﬁrst described the phenomenon it represents, is a two-qubit entangled quantum

state that has some unique properties.The most common Bell state are:

singlet state:

√

|ϕ> = (|01> − |10>)1/ 2

Triplet state:

√

|ϕ> = (|01> + |10>)1/ 2



<a name="br4"></a> 

10 QUANTUM GATES

4

√

Figure 2. (|01>-|10>)/ 2

√

Figure 3. (|01>+|10>)/ 2

This instantaneous correlation between the two qubits, even if they are separated by large

distances, is what Einstein referred to as "spooky action at a distance" and is one of the most

fascinating and puzzling aspects of quantum mechanics. The Bell state is a fundamental resource

in quantum computing and quantum communication, as it can be used to perform tasks such as

teleportation and superdense coding.

10\. Quantum Gates

Quantum gates are the basic building blocks of quantum circuits. They are the equivalent

of classical logic gates in classical computing. Quantum gates are represented as matrices that

operate on quantum states, which are represented as vectors.some important quantum gates:

10\.1. Pauli gates

Pauli gates are a group of quantum gates that are named after the physicist Wolfgang Pauli.

There are three Pauli gates: Pauli-X (or NOT) gate, Pauli-Y gate, and Pauli-Z gate. Each gate

performs a speciﬁc operation on a single qubit.



<a name="br5"></a> 

10\.2 Hadamard gate

5

10\.1.1. Pauli-X gate

Pauli-X gate is also called Not gate because it do the same work of ﬂipping state from 0 to 1

and 1 to 0.

ꢀ

ꢁ

0

1

1

0

X =

10\.1.2. Pauli-Y gate

ꢀ

ꢁ

0

i

−i

Y =

0

10\.1.3. Pauli-Z gate

10\.2. Hadamard gate

ꢀ

ꢁ

1

0

0

−1

Z =

This gate is used to create superpositions of quantum states. It maps the basis states |0〉 and

|1〉 to an equal superposition of both states. The Hadamard gate is represented by the following

matrix:

ꢀ

ꢁ

√

1

1

1

−1

H = 1/ 2

10\.3. CNOT gate

This gate is a two-qubit gate that ﬂips the second qubit if the ﬁrst qubit is in the state |1〉.

The CNOT gate is represented by the following matrix:





1

0

0

0

0

1

0

0

0

0

0

1

0

0

1

0









CNOT =





10\.4. Rotation gate

This gates are single-qubit quantum gates commonly used in quantum computing. They are

rotation gates around the axes .

10\.4.1. R<sub>x</sub> gate

ꢀ

ꢁ

cos(θ/2)

−i sin(θ/2)

−i sin(θ/2)

cos(θ/2)

R<sub>x</sub>(θ) =

10\.4.2. R<sub>y</sub> gate

ꢀ

ꢁ

cos(θ/2) − sin(θ/2)

sin(θ/2) cos(θ/2)

R<sub>y</sub>(θ) =



<a name="br6"></a> 

11 SOME COMMON SPIN CORRELATION FUNCTIONS

6

10\.4.3. R<sub>z</sub> gate

ꢀ

ꢁ

e<sup>−iϕ/2</sup>

0

<sup>R</sup>z<sup>(ϕ) =</sup>

0

e<sup>iϕ/2</sup>

11\. Some common spin Correlation functions

We basically going to create quantum circuits to estimate the values of various spin correlation

√

√

functions for the states|00 >, |11 >, 1/ 2(|01 > +|10 >), 1/ 2(|01 > −|10 >).On the IBM quan-

tum computer, each circuit was run 1024 times. The expectation values were calculated as the

diﬀerence between the fraction of 00 and 11 results and the fraction of 01 and 10 results.. When

we measure in the x-z plane of the Bloch sphere, θ in the range(from 0 to π)in intervals of π/16.

When we measure in the x-y plane of the Bloch sphere, we varied ϕ in the range from 0 to 2ϕ in

intervals of π/8.

11\.1. < Z ⊗ σ<sub>θ</sub> >

ꢀ

ꢁ

ꢀ

ꢁ

ꢀ

ꢀ

ꢁ

ꢀ

ꢁ

1 1

0

cos(θ)

sin(θ)

1 cos(θ)

sin(θ)

1

0

0

−1

Z ⊗ σ<sub>θ</sub> =

⊗

\+

⊗

2 0 −1

sin(θ) − cos(θ)

sin(θ)

2 sin(θ) − cos(θ)





ꢀ

ꢀ

ꢁ

ꢁ 

cos(θ)

cos(θ)

sin(θ)

1 ·

0 ·

0 ·



1

2

sin(θ) − cos(θ)

sin(θ) − cos(θ)



ꢁ

ꢀ

ꢁ

\=





cos(θ)

sin(θ)

cos(θ)

sin(θ)

−1 ·

sin(θ) − cos(θ)

sin(θ) − cos(θ)





ꢀ

ꢁ

ꢀ

ꢁ 



1

0

1

0

0

1

0

0

−1

cos(θ) ·

sin(θ) ·

sin(θ) ·

1

−1



ꢀ

ꢁ

ꢀ

ꢁ

\+





2

0

1

0

0

− cos(θ) ·

−1

−1





cos(θ)

0

sin(θ)

0

0





1

2

0

sin(θ)

0

− cos(θ)

− sin(θ)





\=





0

− cos(θ)

0

cos(θ)

− sin(θ)

0

for product states:< Z ⊗ σ >= cos θ

θ

for entangled state:< Z ⊗ σ >= − cos θ

θ

circuit to perform measurements for estimation of expectation value:

0

0

H

•

R<sub>y</sub>(θ)

•

H

H

H

Code to perform a experiment to calculate expectation value < z ⊗ σ > we create a circuit

θ

and than run this circuit for various states 1024 times to get results:

Listing 1: Code

import numpy as np

from q i s k i t import QuantumCircuit , Aer , execute

\# Define the s t a t e s to measure

s t a t e s = [ ’ 00 ’ , ’ 11 ’ , ’01+10 ’ , ’01−10 ’ ]

\# Define the range of theta values to measure

theta\_vals = np . arange (0 , np . pi , np . pi /16)

\# Define the quantum c i r c u i t



<a name="br7"></a> 

11\.1 < Z ⊗ σ<sub>θ</sub> >

7

qc = QuantumCircuit (2 , 1)

for state in s t a t e s :

print ( f " Expectation ␣ values ␣ for ␣ state ␣{ state }: " )

for theta in theta\_vals :

\# Prepare the i n i t i a l s t a t e

i f state == ’ 00 ’ :

pass

e l i f state == ’ 11 ’ :

qc . x (0)

qc . x (1)

e l i f state == ’01+10 ’ :

qc . h (0)

qc . cx (0 ,1)

e l i f state == ’01−10 ’ :

qc . x (0)

qc . h (1)

qc . cx (0 ,1)

\# Apply the Z tensor product sigma theta gate

qc . rz ( theta , 1)

qc . cx (0 , 1)

qc . h (0)

qc . measure (0 , 0)

\# Run the c i r c u i t on a quantum simulator

simulator = Aer . get\_backend ( ’ qasm\_simulator ’ )

r e s u l t = execute ( qc , backend=simulator , shots =1024). r e s u l t ()

counts = r e s u l t . get\_counts ( qc )

\# Calculate the expectation value

i f ’ 0 ’ in counts :

exp\_val = ( counts [ ’ 0 ’ ]/1024) − 0.5

else :

exp\_val = −0.5

print ( f " Theta ␣=␣{ theta : . 2 f } , ␣ Expectation ␣ value ␣=␣{ exp\_val : . 4 f }" )

\# Reset the quantum c i r c u i t for the next measurement

qc . r e s e t ()



<a name="br8"></a> 

11\.2 < σ ⊗ σ >

8

θ

θ

11\.2. < σ ⊗ σ >

θ

θ

ꢀ

ꢁ

ꢀ

sin(θ)

ꢁ

cos(θ)

sin(θ)

cos(θ)

sin(θ)

σ ⊗ σ =

⊗

θ

θ

sin(θ) − cos(θ)

sin(θ) − cos(θ)



ꢀ

ꢁ

ꢀ

ꢁ 



cos(θ)

cos(θ)

sin(θ)

cos(θ) ·

sin(θ) ·

sin(θ) ·



sin(θ) − cos(θ)

sin(θ) − cos(θ)



ꢀ

ꢁ

sin(θ) cos(θ) sin(θ) cos(θ)

ꢀ

ꢁ

\=

\=





cos(θ)

sin(θ)

cos(θ)

sin(θ) − cos(θ)

sin(θ)

− cos(θ) ·

sin(θ) − cos(θ)







cos<sup>2</sup>(θ)

sin (θ)

sin(θ) cos(θ)

sin(θ) cos(θ)

cos<sup>2</sup>(θ)

2

2

2



sin(θ) cos(θ)

sin(θ) cos(θ)

sin<sup>2</sup>(θ)

− sin (θ)

− cos (θ)







2

2



− cos (θ)

− sin (θ)

sin(θ) cos(θ) sin(θ) cos(θ)

circuit diagram:

for product state:< σ ⊗ σ >= cos<sup>2</sup> θ

θ

θ

for other triplet states:< σ ⊗ σ >= 1 − 2 cos<sup>2</sup> θ

θ

θ

for singlet state:< σ ⊗ σ >= −1

θ

θ

Listing 2: Code

import numpy as np

from q i s k i t import QuantumCircuit , Aer , execute

\# Define the s t a t e s to measure

s t a t e s = [ ’ 00 ’ , ’ 11 ’ , ’01+10 ’ , ’01−10 ’ ]

\# Define the range of theta values to measure

theta\_vals = np . arange (0 , np . pi , np . pi /16)

\# Define the quantum c i r c u i t



<a name="br9"></a> 

11\.2 < σ ⊗ σ >

9

θ

θ

qc = QuantumCircuit (2 , 1)

for state in s t a t e s :

print ( f " Expectation ␣ values ␣ for ␣ state ␣{ state }: " )

for theta in theta\_vals :

\# Prepare the i n i t i a l s t a t e

i f state == ’ 00 ’ :

pass

e l i f state == ’ 11 ’ :

qc . x (0)

qc . x (1)

e l i f state == ’01+10 ’ :

qc . h (0)

qc . cx (0 ,1)

e l i f state == ’01−10 ’ :

qc . x (0)

qc . h (1)

qc . cx (0 ,1)

\# Apply the sigma theta tensor product sigma theta gate

qc . rx ( theta , 0)

qc . rx ( theta , 1)

qc . cx (0 , 1)

qc . h (0)

qc . measure (0 , 0)

\# Run the c i r c u i t on a quantum simulator

simulator = Aer . get\_backend ( ’ qasm\_simulator ’ )

r e s u l t = execute ( qc , backend=simulator , shots =1024). r e s u l t ()

counts = r e s u l t . get\_counts ( qc )

\# Calculate the expectation value

i f ’ 0 ’ in counts :

exp\_val = ( counts [ ’ 0 ’ ]/1024) − 0.5

else :

exp\_val = −0.5

print ( f " Theta ␣=␣{ theta : . 2 f } , ␣ Expectation ␣ value ␣=␣{ exp\_val : . 4 f }" )

\# Reset the quantum c i r c u i t for the next measurement

qc . r e s e t ()



<a name="br10"></a> 

11\.3 X ⊗ σ<sub>ϕ</sub>

10

11\.3. X ⊗ σ<sub>ϕ</sub>

ꢀ

ꢁ

cos(ϕ)

ꢀ

ꢁ

0

1

1

0

cos(ϕ)

sin(ϕ)

X ⊗ σ<sub>ϕ</sub> =

⊗

sin(ϕ) − cos(ϕ)



ꢀ

ꢁ

ꢀ

ꢁ



sin(ϕ)

cos(ϕ)

sin(ϕ)

0 ·

1 ·

1 ·

0 ·



sin(ϕ) − cos(ϕ)

sin(ϕ) − cos(ϕ)



ꢀ

ꢁ

sin(ϕ)

ꢀ

ꢁ

\=





cos(ϕ)

sin(ϕ)

cos(ϕ)

sin(ϕ)

sin(ϕ) − cos(ϕ)

sin(ϕ) − cos(ϕ)

0

sin(ϕ)







0

cos(ϕ)



cos(ϕ)

sin(ϕ)

0

0

0

0

0





\=





− cos(ϕ)

sin(ϕ) − cos(ϕ)

0

for product state:< X ⊗ σ = 0 >

ϕ

for other triplet state:< X ⊗ σ = cos ϕ >

ϕ

for singlet state:< X ⊗ σ = − cos ϕ >

ϕ

code to experimentally calculate < X ⊗ σ >for the given states, run the circuit 1024 times

ϕ

on a quantum processor, and vary phi from 0 to 2π in intervals of π/8 when measuring in the x-y

plane of the Bloch sphere:

Listing 3: Code

import numpy as np

from q i s k i t import QuantumCircuit , Aer , execute

\# Define the s t a t e s to measure

s t a t e s = [ ’ 00 ’ , ’ 11 ’ , ’01+10 ’ , ’01−10 ’ ]

\# Define the range of phi values to measure

phi\_vals = np . arange (0 , 2∗np . pi , np . pi /8)

\# Define the quantum c i r c u i t

qc = QuantumCircuit (2 , 1)

for state in s t a t e s :



<a name="br11"></a> 

11\.3 X ⊗ σ<sub>ϕ</sub>

print ( f " Expectation ␣ values ␣ for ␣ state ␣{ state }: " )

11

for phi in phi\_vals :

\# Prepare the i n i t i a l s t a t e

i f state == ’ 00 ’ :

pass

e l i f state == ’ 11 ’ :

qc . x (0)

qc . x (1)

e l i f state == ’01+10 ’ :

qc . h (0)

qc . cx (0 ,1)

e l i f state == ’01−10 ’ :

qc . x (0)

qc . h (1)

qc . cx (0 ,1)

\# Apply the X tensor product sigma phi gate

qc . rx (np . pi /2 , 0)

qc . rx ( phi , 1)

qc . cx (0 , 1)

qc . h (0)

qc . measure (0 , 0)

\# Run the c i r c u i t on a quantum simulator

simulator = Aer . get\_backend ( ’ qasm\_simulator ’ )

r e s u l t = execute ( qc , backend=simulator , shots =1024). r e s u l t ()

counts = r e s u l t . get\_counts ( qc )

\# Calculate the expectation value

i f ’ 0 ’ in counts :

exp\_val = ( counts [ ’ 0 ’ ]/1024) − 0.5

else :

exp\_val = −0.5

print ( f "Phi ␣=␣{ phi : . 2 f } , ␣ Expectation ␣ value ␣=␣{ exp\_val : . 4 f }" )

\# Reset the quantum c i r c u i t for the next measurement

qc . r e s e t ()



<a name="br12"></a> 

11\.4 < σ ⊗ σ >

12

ϕ

ϕ

11\.4. < σ ⊗ σ >

ϕ

ϕ

ꢀ

ꢁ

ꢀ

sin(ϕ)

ꢁ

cos(ϕ)

sin(ϕ)

cos(ϕ)

sin(ϕ)

σ ⊗ σ =

⊗

ϕ

ϕ

sin(ϕ) − cos(ϕ)

sin(ϕ) − cos(ϕ)



ꢀ

ꢁ

ꢀ

ꢁ 



cos(ϕ)

cos(ϕ)

sin(ϕ)

cos(ϕ) ·

sin(ϕ) ·

sin(ϕ) ·



sin(ϕ) − cos(ϕ)

sin(ϕ) − cos(ϕ)



ꢀ

ꢁ

sin(ϕ) cos(ϕ) sin(ϕ) cos(ϕ)

ꢀ

ꢁ

\=

\=





cos(ϕ)

sin(ϕ)

cos(ϕ)

sin(ϕ) − cos(ϕ)

sin(ϕ)

− cos(ϕ) ·

sin(ϕ) − cos(ϕ)







cos<sup>2</sup>(ϕ)

sin (ϕ)

sin(ϕ) cos(ϕ)

sin(ϕ) cos(ϕ)

cos<sup>2</sup>(ϕ)

2

2

2



sin(ϕ) cos(ϕ)

sin(ϕ) cos(ϕ)

sin<sup>2</sup>(ϕ)

− sin (ϕ)

− cos (ϕ)







2

2



− cos (ϕ)

− sin (ϕ)

sin(ϕ) cos(ϕ) sin(ϕ) cos(ϕ)

for product state:< σ ⊗ σ >= 0

ϕ

ϕ

for other triplet state:< σ ⊗ σ >= 1

ϕ

ϕ

for singlet state:< σ ⊗ σ >= −1

ϕ

ϕ

code to experimentally calculate < σ ⊗ σ >for the given states, run the circuit 1024 times

ϕ

ϕ

on a quantum processor and vary phi from 0 to 2π in intervals of π/8 when measuring in the x-y

plane of the Bloch sphere:

Listing 4: Code

import numpy as np

from q i s k i t import QuantumCircuit , Aer , execute

\# Define the s t a t e s to measure

s t a t e s = [ ’ 00 ’ , ’ 11 ’ , ’01+10 ’ , ’01−10 ’ ]

\# Define the range of phi values to measure

phi\_vals = np . arange (0 , 2∗np . pi , np . pi /8)

\# Define the quantum c i r c u i t



<a name="br13"></a> 

11\.4 < σ ⊗ σ >

13

ϕ

ϕ

qc = QuantumCircuit (2 , 1)

for state in s t a t e s :

print ( f " Expectation ␣ values ␣ for ␣ state ␣{ state }: " )

for phi in phi\_vals :

\# Prepare the i n i t i a l s t a t e

i f state == ’ 00 ’ :

pass

e l i f state == ’ 11 ’ :

qc . x (0)

qc . x (1)

e l i f state == ’01+10 ’ :

qc . h (0)

qc . cx (0 ,1)

e l i f state == ’01−10 ’ :

qc . x (0)

qc . h (1)

qc . cx (0 ,1)

\# Apply the sigma phi tensor product sigma phi gate

qc . ry ( phi , 0)

qc . ry ( phi , 1)

qc . measure (0 , 0)

\# Run the c i r c u i t on a quantum simulator

simulator = Aer . get\_backend ( ’ qasm\_simulator ’ )

r e s u l t = execute ( qc , backend=simulator , shots =1024). r e s u l t ()

counts = r e s u l t . get\_counts ( qc )

\# Calculate the expectation value

i f ’ 0 ’ in counts :

exp\_val = ( counts [ ’ 0 ’ ]/1024) − 0.5

else :

exp\_val = −0.5

print ( f "Phi ␣=␣{ phi : . 2 f } , ␣ Expectation ␣ value ␣=␣{ exp\_val : . 4 f }" )

\# Reset the quantum c i r c u i t for the next measurement

qc . r e s e t ()



<a name="br14"></a> 

12 QUANTUM EXPERIMENT TO CALCULATE < W|σ ⊗ σ ⊗ σ |W >

14

θ

θ

θ

12\. quantum experiment to calculate < W|σ ⊗ σ ⊗ σ |W >

θ

θ

θ

This circuit is to create

√

|W >= 1/ 3(|001 > +|010 > +|100 >)

0

0

0

1

H

H

H

X

•

•

H

H

H

•

•

•

H

H

H

•

•

•

H

H

H

X

•

•

σ<sub>θ</sub>

•

•

X

after creating this quantum state we use a qiskit code to perform the experiment and plot the

result.

Listing 5: Code

from q i s k i t import QuantumCircuit , execute , Aer

import numpy as np

\# Create the |W> s t a t e

def w\_state ( qc , qubits ) :

n = len ( qubits )

qc . h( qubits [ 0 ] )

for i in range (1 , n ) :

qc . cx ( qubits [ 0 ] , qubits [ i ] )

return qc

\# Define the c i r c u i t to measure <W | (

def sigma\_theta\_circuit ( theta ) :

qubits = range (3)

) | W>

qc = QuantumCircuit ( len ( qubits ) , len ( qubits ))

\# Create the |W> s t a t e



<a name="br15"></a> 

13 CONCLUSION

15

qc = w\_state ( qc , qubits )

\# Apply the tensor product of sigma\_theta operators

qc . s ( qubits [ 0 ] )

qc . s ( qubits [ 1 ] )

qc . s ( qubits [ 2 ] )

qc . h( qubits )

qc . cz ( qubits [ 0 ] , qubits [ 1 ] )

qc . cz ( qubits [ 1 ] , qubits [ 2 ] )

\# Measure the c i r c u i t

qc . measure ( qubits , qubits )

return qc

\# Estimate the expectation value of <W | (

def estimate\_sigma\_theta ( theta ) :

qc = sigma\_theta\_circuit ( theta )

shots = 1024

) |W>

backend = Aer . get\_backend ( ’ qasm\_simulator ’ )

job = execute ( qc , backend , shots=shots )

counts = job . r e s u l t ( ) . get\_counts ( qc )

numerator = counts . get ( ’ 000 ’ , 0) + counts . get ( ’ 011 ’ , 0) + counts . get ( ’ 101 ’ , 0) + c

denominator = counts . get ( ’ 001 ’ , 0) + counts . get ( ’ 010 ’ , 0) + counts . get ( ’ 100 ’ , 0) +

expectation\_value = ( numerator − denominator ) / shots

return expectation\_value

\# Main code to loop over theta values and estimate the expectation value

theta\_values = np . arange (0 , np . pi , np . pi /18)

r e s u l t s = [ ]

for theta in theta\_values :

expectation\_value = estimate\_sigma\_theta ( theta )

r e s u l t s . append ( expectation\_value )

\# Plot the r e s u l t s

import matplotlib . pyplot as plt

plt . plot ( theta\_values , r e s u l t s )

plt . xlabel ( ’ Theta ’ )

plt . ylabel ( ’ Expectation ␣ value ’ )

plt . show ()

on compiling and running this code in IBM quantum lab we got this graph:

13\. Conclusion

These experiments demonstrate the entanglement, measurement probabilities, and unitary ba-

sis transformation operations that are common to all quantum mechanical systems. In this project,

I worked on various concepts of quantum computation which are too much interesting, We have



<a name="br16"></a> 

REFERENCES

16

investigated how IBM quantum computers can be used to determine the spin correlations of quan-

tum systems. We created circuits that mimic the detection of spin correlations in diverse quantum

systems using the quantum gates and measurements oﬀered by the IBM Quantum Experience.

By examining the correlation of spins in a number of systems, including straightforward one-

qubit systems and more intricate multi-qubit systems, we have shown the viability of these circuits.

Our ﬁndings demonstrate the usefulness of these circuits for simulating spin correlations in quantum

systems by demonstrating that the measurement results obtained from these circuits closely match

theoretical predictions. Our ﬁndings show the potential of these technologies for expanding our

knowledge of quantum systems and their behaviour, even though there are still certain limits to

the current level of quantum computing, such as the limited number of available qubits and the

existence of noise in the measurements.

References

[1] Calculating spin correlations with a quantum computer Jed Brody, and Gavin Guzman Avail-

able: https://pubs.aip.org/aapt/ajp/article/89/1/35/1045711/Calculating-spin-correlations-

with-a-quantum

[2] M.

tum

A.Nielsen

Information

and

I.Chuang,

Brody,

Quantum

and

Computation

Gavin Guzman

and

Quan-

Available:

Jed

http://mmrc.amss.cas.cn/tlb/201702/W020170224608149940643.pdf

[3] Introduction to Quantum Mechanics Textbook by David J. Griﬃths

[4] The IBM quantum processors are accessed here: <https://quantum-computing.ibm.com/>.

[5] qiskit documentation and textbook Available: https://qiskit.org/documentation/


