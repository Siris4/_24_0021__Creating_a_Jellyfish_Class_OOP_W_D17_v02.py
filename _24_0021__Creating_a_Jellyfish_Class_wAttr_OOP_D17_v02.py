class Jellyfish:
    def __init__(self, name, length, diameter):
        self.name = name
        self.length = length
        self.diameter = diameter

    def get_name(self):
        return self.name

    def get_length(self):
        return self.length

    def set_diameter(self, diameter):
        self.diameter = diameter  # Set the new diameter

j1 = Jellyfish("Tod", 34, 20)
print(j1.get_name(), j1.get_length())

# Create a Jellyfish instance and call its methods
j2 = Jellyfish("Tina", 25, 18)
print(j2.get_name(), j2.get_length())
j2.set_diameter(22)
print(j2.diameter)  # Prin