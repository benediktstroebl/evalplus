```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers,
    :param delimiter: positive integer
    :return: list of integers with the specified separator
    """
    numbers = [x for x in numbers if x != 0]  # Ensure only non-zero values
    return [x + delimiter for x, delimiter in zip(numbers, [delimeter for _ in range(len(numbers))])]

# Test the function
numbers = [4, 2, 8, 3]
print(intersperse(numbers, 4))  # Expected output: [4, 8, 12, 16]
```