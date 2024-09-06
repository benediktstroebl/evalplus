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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the running balance by adding the `op`. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went below zero at some point. If no such scenario is encountered, it returns `False` at the end of processing all operations, implying that the account balance never went below zero. 

This solution is concise and straightforward, and it correctly solves the problem as described. It can be tested like this:
```python
>> below_zero([1, 2, 3])
False
>> below_zero([1, 2, -4, 5])
True
``` 
The first test confirms that the balance never goes below zero for the input `[1, 2, 3]`, and the second test shows that the balance goes below zero for the input `[1, 2, -4, 5]`.