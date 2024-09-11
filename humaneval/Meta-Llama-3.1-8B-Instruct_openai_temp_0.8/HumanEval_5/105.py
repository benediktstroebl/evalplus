```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers (List[int]): Input list of integers.
        delimiter (int): The number to insert between elements.

    Returns:
        List[int]: List with delimiter inserted between elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # if list is empty, return it as is
        return numbers
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers and an integer delimiter as input. It inserts the delimiter between every two consecutive elements in the input list and returns the resulting list. The function uses a simple and efficient approach by initializing the result list with the first element of the input list and then extending the result list with the delimiter and each subsequent element from the input list.