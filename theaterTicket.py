# Constants for seat layout
NUM_COLUMNS = 8
NUM_ROWS = 9

# Function to display the seating arrangement
def display_seating(array):
    all_sold_out = True  # Flag to check if all seats are sold out
    for row in range(NUM_ROWS - 1, -1, -1):  # Reverse rows (start from last row)
        for col in range(NUM_COLUMNS):
            if array[row][col] == 0:  # Seat is sold out
                print(" X", end="    ")
            else:
                print(f"${array[row][col]}", end="   ")
                all_sold_out = False
        print()
    
    # If all seats are sold out, display sold out message
    if all_sold_out:
        print("\nTheater is sold out!")

# Function to select a seat
def select_seat(array):
    while True:
        try:
            row = int(input("Select Row (1-9): ")) - 1
            col = int(input("Select Column (1-8): ")) - 1
            if 0 <= row < NUM_ROWS and 0 <= col < NUM_COLUMNS:
                if array[row][col] != 0:  # If seat is available
                    print(f"Ticket price: ${array[row][col]}")
                    array[row][col] = 0  # Mark the seat as sold
                    break
                else:
                    print("Seat already sold, try again.")
            else:
                print("Invalid seat, try again.")
        except ValueError:
            print("Invalid input, please enter valid numbers.")

# Function to sell out all tickets immediately
def sell_out_immediately(array):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            array[row][col] = 0  # Mark all seats as sold
    print("All tickets have been rented out by Ryan!\n")

# Main function
def main():
    # Initial seating arrangement (price per seat)
    seating = [
        [40, 50, 50, 50, 50, 50, 50, 40],
        [30, 30, 40, 50, 50, 40, 30, 30],
        [20, 30, 30, 40, 40, 30, 30, 20],
        [10, 20, 20, 20, 20, 20, 20, 10],
        [10, 20, 20, 20, 20, 20, 20, 10],
        [10, 20, 20, 20, 20, 20, 20, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10]
    ]
    
    while True:
        print("\nAvailable Theater Seating:")
        display_seating(seating)
        
        # Ask if the user wants to sell out all tickets immediately
        choice = input("Do you want to sell out all tickets immediately? (y/n): ").strip().lower()
        if choice == 'y':
            sell_out_immediately(seating)
            display_seating(seating)
            break
        
        # Otherwise, proceed with seat selection
        select_seat(seating)
        
      


main()
