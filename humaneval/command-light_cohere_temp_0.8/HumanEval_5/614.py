```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1)

# Test cases
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
print(f'Test 1: {expected}', end='')

numbers = [4, 5, 6]
delimiter = 3
expected = [4, 5, 6, 12]
print(f'Test 2: {expected}', end='')

numbers = [1, 2, 3]
delimiter = 6
expected = [1, 2, 6, 12, 3]
print(f'Test 3: {expected}', end='')

```
This code defines a Python function `intersperse` that separates a list of numbers using a specified delimiter. The `numbers` list is passed as an argument, and the `delimiter` is the number to be inserted between every pair of consecutive elements. The `expected` list holds the results of the `intersperse` function for each test case.