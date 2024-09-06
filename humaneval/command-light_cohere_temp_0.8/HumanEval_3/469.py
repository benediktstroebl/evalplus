```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Tests
#example usage
operations = [1, 2, -4, 5]
has_negative_balance = below_zero(operations)
print(has_negative_balance) # Output: True
``` 
This function below_zero uses a loop to iterate through a list of operations, then at each step, it will subtract the operation from the balance. If the balance becomes below zero, the function will return True, else it will return False.