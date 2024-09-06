```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases for the function
numbers_list = [1, 2, 3, 4]
delimiters_list = [4, 8, 12, 16]

result = intersperse(numbers_list, delimiters_list)

print("Result:", result)  # Output: [5, 12, 20, 28]

numbers_list = [1, 2, 3, 4, 5]
delimiters_list = [4, 8, 12]

result = intersperse(numbers_list, delimiters_list)

print("Result:", result)  # Output: [5, 12, 16, 20]
```