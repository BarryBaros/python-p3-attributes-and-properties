#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Mutt"):
        self._name = None  
        self._breed = None  
        self.name = name  
        self.breed = breed  

   
    def name(self):
        return self._name

  
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

   
    def breed(self):
        return self._breed

    
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Example usage
rex = Dog("Rex", "Poodle")
print(rex.name)  # Output: Rex
print(rex.breed)  # Output: None, because Poodle is not in the approved breeds list

jelly = Dog("Jelly", "Corgi")
print(jelly.name)  # Output: Jelly
print(jelly.breed)  # Output: Corgi

invalid_dog = Dog("A" * 10, "Mutt")  # Name is too long
print(invalid_dog.name)  # Output: None, because name is invalid
