```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the consecutive elements.

    Returns:
    List[int]: The list with the delimeter inserted between the consecutive elements.

    Example:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        if num!= numbers[-1]:  # Check if it's not the last element
            result.append(delimeter)
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a simple loop to iterate over the input list, appending each number and the delimeter to the result list. The test cases at the end demonstrate the function's behavior.