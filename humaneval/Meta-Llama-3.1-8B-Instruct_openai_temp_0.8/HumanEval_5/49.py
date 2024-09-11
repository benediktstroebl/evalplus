### Interspersing Elements in a List
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
    - numbers (List[int]): The input list of integers
    - delimeter (int): The number to be inserted between consecutive elements

    Returns:
    - List[int]: The list with the delimeter inserted between consecutive elements

    Example:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # Return empty list if input list is empty

    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    return result[:-1]  # Remove the extra delimeter at the end

# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```
This script defines a function `intersperse` that takes a list of integers and a number as input, and returns a new list with the given number inserted between every two consecutive elements of the input list. It handles the edge case where the input list is empty, in which case it returns the empty list.