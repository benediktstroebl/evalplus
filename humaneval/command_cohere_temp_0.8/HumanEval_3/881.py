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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance goes negative at any point, the function returns `True`. Otherwise, it returns `False`. The script passes the given tests of returning `False` for the first test and `True` for the second test. 
The function returns `False` since the balance is never below zero. 

Here is an example of how to use the code provided:
```python
def test_below_zero():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
``` 
This would run the above function tests.