```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

The `below_zero` function iterates through the list of `operations`, summing them to the running total `balance`. Whenever the `balance` falls below zero, it returns `True`. Otherwise, it returns `False` at the end of the loop if the balance remained non-negative. 

This approach takes advantage of the short-circuit evaluation of Python logical operators, where `True` values are immediately returned whenever they are encountered, and the loop is skipped. 

This solution has a time complexity of `O(n)` since it requires iterating through each element in the list once. 

To test this script, copy and paste it into a Python file (e.g., `problem.py`). You can then execute the file in your Python environment. Here's an example of how you can use the `below_zero` function:
```python
from problem import below_zero

# Test case 1: Should return False
print(below_zero([1, 2, 3]))  # Output: False

# Test case 2: Should return True
print(below_zero([1, 2, -4, 5]))  # Output: True
``` 
This will help you verify the correctness of the solution.