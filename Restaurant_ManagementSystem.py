class RestaurantManagementSystem:
    def __init__(self, restaurant_name, location, cuisine_type):
        self.restaurant_name = restaurant_name
        self.location = location
        self.cuisine_type = cuisine_type
        self.tables = {
            'T1': None, 'T2': None, 'T3': None, 'T4': None, 'T5': None,
            'T6': None, 'T7': None, 'T8': None, 'T9': None, 'T10': None
        }

    def display_info(self):
        print(f"\nRestaurant: {self.restaurant_name}")
        print(f"Location: {self.location}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def display_tables(self):
        print("\nAvailable Tables:")
        for table, status in self.tables.items():
            if status is None:
                print(table, end=' ')
        print()

    def reserve_table(self):
        self.display_tables()
        table_number = input("Enter table number to reserve (e.g., 'T1'): ").strip().upper()

        if table_number not in self.tables:
            print("Invalid table number. Please try again.")
            return

        if self.tables[table_number] is None:
            customer_name = input("Enter customer name: ").strip()
            self.tables[table_number] = customer_name
            print(f"Table {table_number} reserved successfully for {customer_name}")
        else:
            print(f"Table {table_number} is already reserved.")

    def cancel_reservation(self):
        table_number = input("Enter table number to cancel reservation: ").strip().upper()

        if table_number not in self.tables:
            print("Invalid table number. Please try again.")
            return

        if self.tables[table_number] is not None:
            print(f"Cancelled reservation for table {table_number} - {self.tables[table_number]}")
            self.tables[table_number] = None
        else:
            print(f"Table {table_number} is not reserved.")

    def print_bill(self):
        print("\nReservation Details:")
        self.display_info()
        for table, customer in self.tables.items():
            if customer:
                print(f"Table {table}: {customer}")
        print("Thank you for dining with us!")

    def run(self):
        while True:
            print("\nRestaurant Management System")
            print("1. Display restaurant information")
            print("2. Display available tables")
            print("3. Reserve a table")
            print("4. Cancel a reservation")
            print("5. Print reservation details and exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.display_info()
            elif choice == '2':
                self.display_tables()
            elif choice == '3':
                self.reserve_table()
            elif choice == '4':
                self.cancel_reservation()
            elif choice == '5':
                self.print_bill()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Main Program
print("Restaurant Management System")

# Cities as Restaurant Locations
restaurants = [
    {"name": "Salem Spice", "location": "Salem", "cuisine": "South Indian"},
    {"name": "Erode Eats", "location": "Erode", "cuisine": "Chettinad"},
    {"name": "Coimbatore Cuisines", "location": "Coimbatore", "cuisine": "Continental"},
    {"name": "Erode Bites", "location": "Erode", "cuisine": "North Indian"}
]

# Display available restaurants
for i, restaurant in enumerate(restaurants, start=1):
    print(f"{i}. {restaurant['name']} ({restaurant['location']}) - {restaurant['cuisine']}")

# Choose a restaurant
restaurant_choice = int(input("Choose a restaurant by number: "))
selected_restaurant = restaurants[restaurant_choice - 1]

# Create restaurant management system for the selected restaurant
restaurant_system = RestaurantManagementSystem(
    selected_restaurant["name"],
    selected_restaurant["location"],
    selected_restaurant["cuisine"]
)

# Run the system
restaurant_system.run()
