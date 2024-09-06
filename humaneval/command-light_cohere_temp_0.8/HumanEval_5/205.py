```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Args:
        numbers (list) : List of integers.
    Args:
        delimiter (int) : Insertion point (number) between consecutive elements
    Returns:
        list : List of integers with the element at even positions separated by 'delimiter'
    """
    return [num + delimiter if i % 2 == 0 else num + delimiter for i, num in enumerate(numbers)]

#Test case 1
input_numbers = [4, 2, 3]
result = intersperse(input_numbers, 4)
assert list(result) == [4, 4, 2, 4, 3]

#Test case 2
input_numbers = [1, 2, 3]
result = intersperse(input_numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]
```