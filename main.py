from pyenigma import enigma
from pyenigma import rotor

print("Machine enigma en Python")

print(rotor.ROTOR_GR_III)

engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AV BS CG DL FU HZ IN KM OW RX")
print(engine)

# secret = engine.encipher("Hello World")
# print(secret)


reflectors = [rotor.ROTOR_Reflector_A, rotor.ROTOR_Reflector_B, rotor.ROTOR_Reflector_C]
for reflector in reflectors:
  engine = enigma.Enigma(reflector, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AV BS CG DL FU HZ IN KM OW RX")
  # print(engine)
  secret = engine.encipher("Hello World")
  print(secret)

print ("A terminer")