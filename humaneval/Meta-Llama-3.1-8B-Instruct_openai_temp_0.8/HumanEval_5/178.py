```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): A list of integers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: A new list with the delimeter inserted between consecutive elements.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Example usage:
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines the `intersperse` function as specified and includes example usage at the end. It uses a simple loop to append each element from the input list to the result list, followed by the delimeter, effectively inserting the delimeter between consecutive elements.