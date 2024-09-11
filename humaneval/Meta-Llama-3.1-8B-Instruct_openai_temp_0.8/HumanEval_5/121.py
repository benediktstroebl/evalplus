```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted between every two consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        if result:  # Check if result list is not empty
            result.append(delimeter)
    return result[:-1] if result else []  # Remove the last delimeter if it exists


# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as per the given specification and includes a test to ensure it behaves as expected. The function uses a simple loop to iterate over the input list, appending each number to the result list and then the delimeter, until it reaches the end of the list. It then returns the result list, removing any trailing delimeter if present.