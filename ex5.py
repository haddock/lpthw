name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
height_in_meters = round(height / 39.7, 2)
weight = 180 #lbs
weight_in_kilograms = round(weight / 2.205)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_in_meters} meters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are ususally {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")