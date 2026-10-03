import pandas as pd
import json
import matplotlib.pyplot as plt

def main():
    # 1. Load Data
    try:
        df = pd.read_csv("data.csv")
        km, price = df['km'].values, df['price'].values
    except FileNotFoundError:
        return print("Error: data.csv not found.")

    # 2. Train Model (Gradient Descent)
    m, lr, epochs = len(km), 0.1, 2000
    t0, t1, max_km = 0.0, 0.0, max(km)
    scaled_km = km / max_km  # Normalize to prevent explosion

    for _ in range(epochs):
        err = (t0 + t1 * scaled_km) - price
        t0 -= lr * sum(err) / m
        t1 -= lr * sum(err * scaled_km) / m

    t1 /= max_km  # Denormalize t1 for raw km input

    # 3. Save Thetas
    with open("thetas.json", "w") as f:
        json.dump({"t0": t0, "t1": t1}, f)

    # 4. Calculate Precision (R-squared)
    preds = t0 + (t1 * km)
    r2 = 1 - (sum((price - preds)**2) / sum((price - price.mean())**2))
    print(f"Training Complete! Precision (R2): {r2 * 100:.2f}%\nt0: {t0:.2f}, t1: {t1:.4f}")

    # 5. Plot Graph
    plt.scatter(km, price, color='blue', label='Actual Data')
    plt.plot(km, preds, color='red', label='Regression Line')
    plt.xlabel('Mileage (km)'), plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()