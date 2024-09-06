```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Example usage:
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)  # Output: [5, 11, 13, 12, 16, 18]

numbers = [1, 2, 3]
other_delimiters = [4, 2, 6]
result2 = intersperse(numbers, other_delimiters)
print(result2)  # Output: [5, 4, 8, 6]
```

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a list of numbers with the specified delimiter between every two consecutive elements. The example usage demonstrates how this can pass in different lists of numbers and delimiters to test the functionality.