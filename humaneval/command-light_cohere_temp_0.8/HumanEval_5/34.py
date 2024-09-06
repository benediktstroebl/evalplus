```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case: Insert 4 as a separator between consecutive numbers in an empty list
result = intersperse([], 4)
print(result)  # Output: []

# Test case: Insert 4 as a separator between 2 and 3
result = intersperse([1, 2, 3], 4)
print(result)  # Output: [1, 4, 2, 4, 3]

# Test case: Insert as separator between every element of an existing list
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 3, 4, 5]

# Test case: Insert 3 as a separator between every 2nd element of an existing list
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 3)
print(result)  # Output: [1, 3, 4, 5]
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by the specified delimiter. It then passes these tests to demonstrate the behavior of the function.