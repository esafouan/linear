import json
import os

def main():
    t0, t1 = 0.0, 0.0
    
    if os.path.exists("thetas.json"):
        with open("thetas.json", "r") as f:
            data = json.load(f)
            t0, t1 = data.get("t0", 0.0), data.get("t1", 0.0)

    while True:
        try:
            km = float(input("Enter mileage (km): "))
            
            if km < 0:
                print("Mileage cannot be negative. Please try again.")
                continue  # Restarts the loop to ask for input again
                
            price = max(0, t0 + (t1 * km)) # Prevent negative prices
            print(f"Estimated price: {price:.2f}")
            break  # Exits the loop after a successful prediction
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()