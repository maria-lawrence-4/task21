# TASK 12 - MARIA LAWRENCE 

# List of menu
menu_list = ['houmous', 'aubergine dip', 'pitta', 'falafel', 'kofta']

# Dictorionary of stock
stock = {'houmous': 2,
              'aubergine dip': 4,
              'pitta': 8, 
              'falafel': 3,
              'kofta': 1
              }

# Dictionary of price
price = {'houmous': 2.20,
              'aubergine dip': 3.10,
              'pitta': 0.50, 
              'falafel': 5.0,
              'kofta': 7.60
              }

total_stock_worth = 0
for items in menu_list:
    item_value = stock[items] * price[items]
    total_stock_worth += item_value

print(f"The total stock worth in the cafe is £{total_stock_worth:.2f}.")


# NB if we wanted to do it for each individual item:

# List of menu

stock_value_individual = {item:stock[item] * price[item] for item in menu_list}

for item in stock_value_individual:
    print(f"You have £{stock_value_individual[item]:.2f} worth of {item.capitalize()}.")