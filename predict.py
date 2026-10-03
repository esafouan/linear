import json
import os

def main():
    t0, t1 = 0.0, 0.0
    
    if os.path.exists("thetas.json"):
        with open("thetas.json", "r") as f:
            data = json.load(f)
            t0, t1 = data.get("t0", 0.0), data.get("t1", 0.0)

    try:
        km = float(input("Enter mileage (km): "))
        price = max(0, t0 + (t1 * km)) # Prevent negative prices
        print(f"Estimated price: {price:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()