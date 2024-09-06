```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers: list of integers, delimiter: integer to be inserted
    Returns:
        list of integers with each consecutive pair separated by 'delimiter'
    """
    return [x + delimiter for x, delimiter in zip(numbers, delimeter)]

# Test the function with different inputs
numbers = [1, 2, 3]
delimiters = [4, 2]
result = intersperse(numbers, delimiters)
print(result)  # expected output: [1, 4, 2, 4, 3]

numbers = [10, 11, 12]
delimiters = [5, 10]
result = intersperse(numbers, delimiters)
print(result)  # expected output: [6, 10, 11, 15, 12]

numbers = [10, 10, 10]
delimiters = [10, 10, 10]
result = intersperse(numbers, delimiters)
print(result)  # expected output: [10, 10, 10, 20]
```