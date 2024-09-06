Here is the Python script that solves the problem of checking for negative balance in a markdown code block:
```python
def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    
    :

    operations = sorted(set(operations))
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```
The function takes a list of operations and returns a boolean indicating whether the balance fell below zero at any point. The function first sorts the string of numbers in the operations list and creates a new list with only the integers (no fractions or decimals). Then the function creates a variable called balance and initializes it to 0. The function then loops through each number in the operations list. If the balance falls below 0, the function returns True. Otherwise, it adds the balance with the number in the operations list and returns False.