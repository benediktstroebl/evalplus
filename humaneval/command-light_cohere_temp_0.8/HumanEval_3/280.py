```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Unit tests
def test_below_zero():
    operations = [1, 2, -4, 5]
    expect = [True, True, True, False]
    assert below_zero(operations) == expect

# Example usage
test_below_zero()
```
This script defines a function `below_zero` that checks whether the balance of an account falls below zero based on a given list of operations. It initializes a example list of operations, and then iterates over the list, checking if the balance falls below zero and returning `True` if so. The function also subtracts each operation from the balance and returns `False` if the balance is still positive after the operation.

Finally, the script provides a unit test `test_below_zero` to check if the `below_zero` function is working correctly with the provided operations. 
The test should return the expected results.