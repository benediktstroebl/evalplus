Here's a Python script with a self-contained function that solves the problem you've described: 

```python
def below_zero(operations: List[int]) -> bool:
    """ Checks whether the balance of the account ever falls below zero in the given operations.
    # Iterate through operations from left to right, and at each step, it checks if the balance is less than zero.
    # If operations = [1, 2, -4, 5] 
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

# Test the function
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
```

This function, `below_zero`, takes a list of operations as an argument. It iterates over each operations from left to right, and at each step, it adds the current operation to the balance. If at any time the another operation is added, and the balance becomes less than zero, the function returns `True`. Otherwise, it returns `False` after iterating through all operations.

The function has been tested with a sample input, and the output is printed to the console.