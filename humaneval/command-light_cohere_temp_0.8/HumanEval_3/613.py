```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
``` 
This function will evaluate the operations on a balance starting at zero, and will return True if any operation would cause the balance to be less than zero. 
You can then test the function using the provided test cases.