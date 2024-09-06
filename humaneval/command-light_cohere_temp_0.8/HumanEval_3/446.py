```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # This will print True
```
The function takes a list of operations as an argument and uses a loop to add each operation to a running balance. The function then returns `True` if the balance becomes less than 0, indicating that the operations resulted in a negative balance. 

To test the function, an example usage is provided, where operations is a list of integers representing deposit and withdrawal operations.