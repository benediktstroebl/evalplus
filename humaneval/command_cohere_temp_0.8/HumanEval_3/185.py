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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the ending balance is less than 0, the function returns `True`. If the ending balance is 0 or positive, the function returns `False`. 

Here is an example usage of the script:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```
This example usage passes the test cases provided in the original problem. Make sure to run the script with Python 3.8 or higher to take advantage of the type hints and other features.