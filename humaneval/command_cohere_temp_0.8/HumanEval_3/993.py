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

The script defines a function `below_zero` that takes in a list of `List[int]` and returns a `bool`. It iterates through each operation in the input list and accumulates them to the `balance` variable. Whenever the balance goes below zero, the function returns `True`. If the balance stays non-negative until the end of the list, it returns `False`. This approach is straightforward and intuitive, using a simple loop and cumulative balance tracking.  This solution should pass both test cases mentioned in the prompt.