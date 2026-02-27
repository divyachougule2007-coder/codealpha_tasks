def stock_portfolio_tracker():
    # Hardcoded stock prices
    prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "AMZN": 3400,
        "MSFT": 300
    }

    portfolio = {}  # Store symbol: quantity
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and their prices:")
    for symbol, price in prices.items():
        print(f"  {symbol}: ${price}")

    # Input loop
    while True:
        symbol = input("\nEnter stock symbol (or press Enter to finish): ").upper().strip()
        if symbol == "":
            break
        if symbol not in prices:
            print(f"Symbol '{symbol}' not found in price list. Please enter a valid symbol.")
            continue

        try:
            quantity = float(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be positive. Try again.")
                continue
        except ValueError:
            print("Invalid number. Please enter a numeric quantity.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    # Calculate total investment value
    total_value = 0.0
    print("\n--- Portfolio Summary ---")
    for symbol, qty in portfolio.items():
        price = prices[symbol]
        value = price * qty
        total_value += value
        print(f"{symbol}: {qty} shares @ ${price} = ${value:.2f}")

    print(f"\nTotal Investment Value: ${total_value:.2f}")

    # Optional save to file
    save_option = input("\nSave to file? (y/n): ").lower().strip()
    if save_option == 'y':
        filename = input("Enter filename (default: portfolio.txt): ").strip()
        if filename == "":
            filename = "portfolio.txt"

        with open(filename, 'w') as f:
            f.write("Stock Portfolio Report\n")
            f.write("======================\n")
            for symbol, qty in portfolio.items():
                price = prices[symbol]
                value = price * qty
                f.write(f"{symbol}: {qty} shares @ ${price} = ${value:.2f}\n")
            f.write(f"\nTotal Investment Value: ${total_value:.2f}\n")
        print(f"Report saved to {filename}")

if __name__ == "__main__":
    stock_portfolio_tracker()
