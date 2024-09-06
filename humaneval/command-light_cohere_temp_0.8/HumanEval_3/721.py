```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

#Test cases
tests = [
    [
        [1, 2, -4, 5],
    [-100, 2, -3],
    [-1, 100, -2],
    [100, -100, 1],
    [1, 2, 3, -1]
]

for test in tests:
    result = below_zero(test)
    print(f"Test {test} - Result: {result}")
```
This script defines a function below_zero that checks if the balance of a bank account falls below zero after applying a list of operations. The function iterates over the by using a loop and sets the balance to zero. If at any point the result is True, the function will return True, otherwise, it will return False.

Additionally, the script has a list of test cases that are passed to the function to test its functionality. The script will then by using the loop, which will iterate over the test cases and display the result of each test.