```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers: List[int] - list of integers
        delimiter: int - number to be inserted

    Returns:
        List[int] - list where elements are spaced by 'delimiter'
    """
    return [num + delimiter for delimiter, num in zip(numbers[1:], numbers[:1])] + numbers

# Test cases
numbers = [1, 2, 3, 4, 5]
print(inperse(numbers, 4))  # Expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3]
print(inperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]

numbers = [10, 20, 30]
print(inperse(numbers, 5))  # Expected output: [10, 15, 20, 25]
```