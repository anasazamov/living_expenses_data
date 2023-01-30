from json import loads

# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    monthly_expenses=loads(monthly_expenses)
    sum=0
    for i in monthly_expenses.values():
        sum+=i
    return sum

f=open("data.json",mode="r").read()

print(total_expenses(f))