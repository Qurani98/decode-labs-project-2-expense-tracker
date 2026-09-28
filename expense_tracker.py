print("=" * 30)
print("       EXPENSE TRACKER")
print("=" * 30)

total = 0

while True:
    expense = input("Enter expense amount (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    total += float(expense)

print("\n" + "=" * 30)
print(f"Total Spent: Rp{total:,.0f}")
print("=" * 30)