```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim  in zip(numbers, [delimeter] * 2)]

# Test cases
numbers = [1, 2, 3]
print(inpersece(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]

numbers = [1000, 10000, 5]
print(inpersece(numbers, 2))  # Expected Output: [1000, 2, 10000, 40000, 5]

# Correct usage with custom delimiters
delimiters = [2, 3]
print(inpersece(numbers, delimiters))  # Expected Output: [1, 2, 3, 2, 3, 5]
```