print("Akshansh Dwivedi")

Computers = {
    "Laptop1": {"brand": "DELL", "OS": "Windows"},
    "Laptop2": {"brand": "HP", "OS": "Linux"},
    "Desktop": {"brand": "Apple", "OS": "Mac-OS"}
}

brand = []
OS = []

for Laptop, Specs in Computers.items():
    brand.append(Specs["brand"])
    OS.append(Specs["OS"])

print("Brands: ", brand)
print("OS: ", OS)