```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases:
numbers = [1, 2, 3, 4, 5]
print(inperseperate(numbers, 3))  # Expected output: [1, 3, 4, 5, 8, 11]

numbers = [1, 2, 3, 4, 5]
print(inperseperate(numbers, 2))  # Expected output: [1, 4, 6, 8, 10]

numbers = [10, 11, 12, 13, 14]
print(inperseperate(numbers, 5))  # Expected output: [10, 15, 18, 21, 28]
```
This script defines a function `inperseperate` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by that delimiter. The test cases demonstrate the example of how the function works. The expected output of each test is the list with numbers separated by the specified delimiter.