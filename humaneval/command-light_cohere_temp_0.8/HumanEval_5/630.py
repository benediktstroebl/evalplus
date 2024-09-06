```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list."""
    return [num + delimeter if index < len(numbers) - 1 else num for index, num in enumerate(numbers)]
# Example usage:
numbers = [1, 2, 3]
delimiters = [4, 4, 2, 4, 3]
result = intersperse(numbers, delimiters)
print(result)  # Expected output: [1, 4, 2, 4, 3, 4, 2, 4, 3]
```