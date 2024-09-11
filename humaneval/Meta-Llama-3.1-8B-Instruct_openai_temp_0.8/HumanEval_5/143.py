```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # start the result with the first element
    for num in numbers[1:]:  # iterate over the rest of the list
        result.extend([delimeter, num])  # add the delimeter and the current number
    return result


# Test the function
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([], 4))  # []
```