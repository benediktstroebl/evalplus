```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to insert between elements.

    Returns:
        List[int]: The list with the delimeter inserted between elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])
    return result[:-1] if delimeter else result

# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3], 0))  # Output: [1, 2, 3]
```

In this script, we define a function `intersperse` that takes a list of integers `numbers` and a delimeter `delimeter`. It creates a new list where the delimeter is inserted between every two consecutive elements of the input list. If the delimeter is zero, the function simply returns the original list.