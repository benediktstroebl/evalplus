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

The `below_zero` function iterates through the list of `operations`, summing them to the `balance`. Whenever the `balance` falls below zero, it returns `True`. Otherwise, it returns `False` at the end of the loop if the `balance` remains non-negative. 

Here is an example usage output:
```python
>> below_zero([1, 2, -4, 5])
True
```
```python
>> below_zero([1, 2, 3])
False
``` 
This script adheres to the problem statement provided and passes the given tests.