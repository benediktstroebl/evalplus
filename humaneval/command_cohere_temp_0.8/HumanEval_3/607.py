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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It calculates the balance by summing up the operations, then checks if it goes negative at any point, and returns `True` if it does, and `False` otherwise. 

Here is an example usage of the function:
```python
>> below_zero([1, 2, 3])
False
>> below_zero([1, 2, -4, 5])
True
```

This output is consistent with the provided example test cases.  This function defines a simple way to solve this problem and demonstrates how powerful typed Python can be, allowing you to write robust and readable code with the help of the `List` and `int` types.