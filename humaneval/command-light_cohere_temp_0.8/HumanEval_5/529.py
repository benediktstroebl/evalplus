```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    return [num + delimiter if index < len(numbers) - 1 else num for index, num in enumerate(numbers)] + [delimiter] * (len(numbers) - 1)

# Test case:
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Expected output: [1, 4, 2, 4, 3]
```