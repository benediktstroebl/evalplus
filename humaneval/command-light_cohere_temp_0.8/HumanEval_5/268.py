```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
    numbers = [1, 2, 3, 4, 5]
    return [i, delimiter, i + delimiter, num] for i, delimiter in enumerate(numbers) + 1]

# Test
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3, 5]
```