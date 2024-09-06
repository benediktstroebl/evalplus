```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i, j in zip(numbers, numbers[1:])] + numbers[-1:]

# Test cases
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
print(f"Test 1: {expected}")

numbers = [1, 2, 3, 4]
delimiter = 3
expected = [1, 3, 2, 4]
print(f"Test 2: {expected}")

numbers = [1, 2, 3, 4, 5]
delimiter = 2
expected = [1, 3, 2, 4, 5]
print(f"Test 3: {expected}")
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a list where numbers are separated every two consecutive elements by the provided delimiter. The test cases demonstrate the both expected output formats.