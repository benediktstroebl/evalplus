```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the consecutive elements.

    Returns:
    List[int]: The list with the specified number inserted between every two consecutive elements.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty, return it immediately
        return numbers
    
    result = [numbers[0]]  # initialize the result list with the first element of the input list
    for i in range(1, len(numbers)):  # iterate over the rest of the elements in the input list
        result.append(delimeter)  # append the delimeter to the result list
        result.append(numbers[i])  # append the current element to the result list
    return result


# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that solves the given problem. The function iterates over the input list, inserting the specified delimeter between every two consecutive elements. If the input list is empty, the function returns it immediately, as specified in the problem. The example usage at the end demonstrates the function's behavior with the provided test cases.