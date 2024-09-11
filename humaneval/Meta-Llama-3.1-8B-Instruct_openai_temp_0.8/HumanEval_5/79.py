```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted between consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    if result:  # Remove the extra delimeter at the end
        result.pop()
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer as input, and returns a new list with the integer inserted between every two consecutive elements of the input list. The `#` character is used to write comments in Python. The test cases at the end of the script demonstrate the function's behavior.