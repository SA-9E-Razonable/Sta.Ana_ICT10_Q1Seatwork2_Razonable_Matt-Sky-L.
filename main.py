from pyscript import display

restaurant_name = "Oishii Nook"
owner_name = "ona Matt Sky-san"
year_since = 2025

menu = [
    ("Crushy Dynamite Roll", "sushi roll packed with shrimp, mushroom, avocado, cucumber and spicy kick", 400.00),
    ("Curry Ramen", "ramen with curry sauce and chicken teriyaki", 500.00),
    ("Yakitori", "grilled chicken skewers", 255.00),
    ("Tempura", "battered and deep fried seafood and vegetables", 385.00),
    ("Donbori (choice of Gyudon or Oyakodon)", "rice bowls topped with beef (gyudon) or chicken and egg (oyakodon)", 600.00)
]

display(restaurant_name, target="name1")  
display(f"Owner: {owner_name}", target="Owner")
display(f"Since {year_since}", target="Since")

for i, (name, desc, price) in enumerate(menu, start=1):
    display(name, target=f"prod{i}")
    display(desc, target=f"desc{i}")
    display(f"PhP {price:,.2f}", target=f"price{i}")