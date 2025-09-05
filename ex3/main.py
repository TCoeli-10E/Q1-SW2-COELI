from pyscript import display


restaurant_name = 'Eleven Madison Park'  # string
owner_name = 'Daniel Humm'  # string
year_established = 1998  # integer
popular_item_price = 365  # integer, in dollars
has_delivery = False  # boolean
product_names = ['Tonburi', 'Grilled turnip', 'Asparagus']  # List, and also outdated because seasonal menu
business_hours = "5:30 - 22:00"     # String
menu_prices = {'5 course': 285, '9 course': 365, 'bar tasting': 225, 'wine pairings': 125, 'Bring your own wine': 75}  # Dictionary, priced in dollars and per guest
common_allergens = ('dairy', 'nuts', 'gluten')  # Tuple
tax_rate = 0.08875  # float, New York City sales tax rate

display(f"{restaurant_name}", target='div1')
display(f"by {owner_name}", target='div2')
display(f"since {year_established}", target='div3')
display(f"open {business_hours}", target='div4')