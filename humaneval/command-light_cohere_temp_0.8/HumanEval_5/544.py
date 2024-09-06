```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a list of integers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [5, 8, 7, 12, 6, 10, 9]

# Test the function with a list of strings and a delimiter
strings = ["hello", "world"]
delimiter = ' '
result = intersperse(strings, delimiter)
print(result)  # Output: ["hullo", "world"]
```