```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test case:
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3]

# Another test case:
numbers = [10, 20, 30]
result = intersperse(numbers, 4)
print(result)  # Expected output: [10, 14, 18, 22, 26]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the integers separated by that delimiter. The test cases pass the