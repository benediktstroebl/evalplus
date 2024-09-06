Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Unit tests
def test_below_zero():
    operations = [1, 2, -4, 5]
    assert below_zero(operations) == True

if __name__ == "__main__":
    test_below_zero()
```
The above Python script contains a below_zero function that checks whether the balance of a bank account falls below zero after processing a list of operations. It uses a the balanced and returns True if the balance becomes negative. The test_below_zero function creates a list of operations and passes it to the below_zero function, which then returns True, indicating that the balance fell below zero during the operations. 
To test the correctness of the below_zero function, the test_below_zero function creates a list of operations and passes it to the below_zero function.