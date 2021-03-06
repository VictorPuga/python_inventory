from utils import (
    safe_input,
    get_products,
    get_employees,
    get_sales
)

# import the main funcions
from actions import (
    register_sale,
    register_product_arrival,
    query_inventory_data,
    employees_with_most_sales,
    most_sold_items,
    show_only_seasonal_products,
    generate_report,
    customer_satisfaction_form
)


def main():
    print("""
Select an action

1. Register sale
2. Register product arrival
3. Query inventory data
4. Most sold items
5. Employees with most sales
6. Generate sales report
7. Show only seasonal products
8. Customer satisfaction form
""")

    while True:
        action = safe_input('int_positive', 'Action: ')

        if action > 0 and action < 9:
            break

        print("Oops! Try again with an action from 1 to 8")

    # action can only be from 1 to 8
    if action == 1:
        register_sale()
    elif action == 2:
        register_product_arrival()
    elif action == 3:
        query_inventory_data()
    elif action == 4:
        most_sold_items()
    elif action == 5:
        employees_with_most_sales()
    elif action == 6:
        generate_report()
    elif action == 7:
        show_only_seasonal_products()
    else:
        customer_satisfaction_form()

    print("\nThanks for using python_inventory. Have a great day\n")


print(" ★ Welcome to Starbucks ★ ")

while True:
    main()

    again = input("Do you want to start again? (y/n) ").lower()

    if 'y' in again:
        continue
    else:
        print("Cool. See you later ;)\n")
        break
