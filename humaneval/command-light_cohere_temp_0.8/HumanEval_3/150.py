Here's the self-contained Python script with a function that solves the problem you've described:

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([6, -10, -20])
    False
    >>> below_zero([100, -100, -1000])
    True
    """
    for num in operations:
        if num < 0:
            return True
    return False
```
The `below_zero` function takes a list of operations and iterates over each element in the list. It checks if the the this element is less than zero, if it is, it returns True, indicating that the balance of the account has fallen below zero. If the loop completes without any negative number being found, the function returns False, indicating that the balance has not fallen below zero.