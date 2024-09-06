```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Parameters: numbers: List[int], delimiter: int
    Returns: List[int]
    """
    return [num, delimiter, num] + [num for _, num in numbers[1:]]

# Test the function with an empty list
test_empty = intersperse([])
assert len(test_empty) == 0

# Test the function with a list of numbers
test_list = intersperse([1, 2, 3, 4, 5])
assert len(test_list) == 5

# Test the function with custom delimiter
test_delimiter = intersperse([1, 2, 3], 4)
assert len(test_delimiter) == 3
```