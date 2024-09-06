```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Args: 
        numbers: list of integers
        delimiter: positive integer
    Returns: 
        list of integers with the delimiter inserted
    """
    result = [num] + [num + delimiter for delimiter in range(delimeter) for num in numbers[1:]] + [num + delimiter] + [num]
    return result

# Test cases
numbers = [1, 2, 3]
print(inspersing(numbers, 4))  # Expected: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(inspersing(numbers, 3))  # Expected: [1, 4, 5, 8, 7]

numbers = [10, 20, 30, 40, 50]
print(inspersing(numbers, 5))  # Expected: [10, 15, 20, 25, 30]
```