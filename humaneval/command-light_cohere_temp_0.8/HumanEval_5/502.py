```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]

# Test the function with a list of integers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Expected output: [0, 4, 2, 4, 6, 3]

# Test the function with a list of strings and an integer delimiter
strings = ["hello", "world"]
delimiter = 3
result = intersperse(strings, delimiter)
print(result)  # Expected output: ["h", "w", "r", "o", "l", "o"]
```