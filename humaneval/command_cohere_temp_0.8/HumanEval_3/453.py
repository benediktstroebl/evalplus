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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the ending balance is less than zero, it returns `True`, otherwise, it returns `False`. 

Here is an example usage of the function:
```python
>> below_zero([1, 2, 3])
False
>> below_zero([1, 2, -4, 5])
True
```

This function will return `True` for the second example given the defined tests.