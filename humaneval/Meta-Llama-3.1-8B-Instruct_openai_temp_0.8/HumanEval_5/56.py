```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): A list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The list with the delimeter inserted

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # initialize the result with the first element
    for num in numbers[1:]:  # iterate over the rest of the elements
        result.extend([delimeter, num])  # insert the delimeter and the current number
    return result


# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that inserts a number `delimeter` between every two consecutive elements of the input list `numbers`. It uses a simple iterative approach to build the resulting list. The function is tested with the provided examples to demonstrate its correctness.