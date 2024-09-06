```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
The function uses a loop to iterate over each element in the operations list, adding each operation to the balance. The function then returns True if the balance is less than 0, and False otherwise.

Please note that this is a self-contained solution, as it doesn't rely on any other functions or modules.  The provided markdown code block was just an example, and you can use this Python function with any list of integers to solve the problem.