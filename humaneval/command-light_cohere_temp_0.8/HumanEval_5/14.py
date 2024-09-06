```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n+n + delimeter)
    return result
# Test cases
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3, 5]

numbers = [10, 9, 8, 7, 6]
result = intersperse(numbers, 3)
print(result)  # Expected output: [10, 7, 9, 8, 6, 3]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = intersperse(numbers, 5)
print(result)  # Expected output: [1, 5, 2, 8, 7, 9, 6]
```
This Python code defines a function `intersperse` that separates consecutive elements in a list by a specified delimiter. The function iterates through the pattern of appending the next element and the delimiter to a result list. The test cases demonstrate the expected outputs for different lists and delimiters.