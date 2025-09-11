from pyscript import display

menu = {
    "Crushy Dynamite Roll": 400.00,
    "Curry Ramen": 500.00,
    "Yakitori": 255.00,
    "Tempura": 385.00,
    "Donbori": 600.00
}

restaurant_name = "Oishii Nook"
owner_name = "ona Matt Sky-san"
year_since = 2025

display(restaurant_name, target="One")
display(f"{owner_name}", target="Owner")
display(f"Since {year_since}", target="Since")
display("Menu and Pricelist", target="heading1")


display("Crushy Dynamite Roll", target="prod1")
display(f"₱{menu['Crushy Dynamite Roll']:.2f}", target="price1")

display("Curry Ramen", target="prod2")
display(f"₱{menu['Curry Ramen']:.2f}", target="price2")

display("Yakitori", target="prod3")
display(f"₱{menu['Yakitori']:.2f}", target="price3")

display("Tempura", target="prod4")
display(f"₱{menu['Tempura']:.2f}", target="price4")

display("Donbori", target="prod5")
display(f"₱{menu['Donbori']:.2f}", target="price5")
