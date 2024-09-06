```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Args:
        numbers: list of integers,
        delimiter: integer, inserted between every two consecutive numbers
    Returns:
        list of integers, with delimiter inserted
    """
    return [num + delimiter for num, delimiter in zip(numbers, [delimeter] * len(numbers))]

# Test the function with a list of integers and a delimiter
numbers = [1, 2, 3]
print(intersperse(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]
```