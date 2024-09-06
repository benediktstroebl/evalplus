Here is the provided Python script:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```

This script defines a function called below_zero that takes a list of operations as input and checks if the balance of the account goes below zero at any point. The function iterates through each operation in the list and updates the balance accordingly. If at any point thees balance goes below zero, the function returns True. Otherwise, it returns False.