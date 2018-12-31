'''
Created on Aug 26, 2015

@author: Emma Howard, for CPT 135

Calculates the momentum of an object by multiplying its mass in kilograms by its velocity in meters per second,
Then also calculates the kinetic energy of the same object using the same inputs
'''

print("Let's find both the momentum and the kinetic energy of an object!")
mass = float(input("Tell me the mass of the object in kilograms: "))
velocity = float(input("Tell me the velocity of the object in meters per second: "))
momentum = mass * velocity
kineticEnergy = .5 * mass * velocity ** 2
print("The momentum is", momentum, "!")
print("The kinetic energy is", kineticEnergy, "!")