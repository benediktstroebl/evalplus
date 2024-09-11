```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): Input list of integers.
    delimiter (int): Number to be inserted between consecutive elements.

    Returns:
    List[int]: List with delimiter inserted between every two consecutive elements.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        if result:
            result.append(delimiter)
        result.append(num)
    return result


def intersperse_itertools(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    This function uses itertools to achieve the same result.

    Args:
    numbers (List[int]): Input list of integers.
    delimiter (int): Number to be inserted between consecutive elements.

    Returns:
    List[int]: List with delimiter inserted between every two consecutive elements.

    Examples:
    >>> intersperse_itertools([], 4)
    []
    >>> intersperse_itertools([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [x for pair in zip(numbers, [delimiter] * len(numbers)) for x in pair][:-1] if numbers else []


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
This script contains two functions: `intersperse` and `intersperse_itertools` to solve the problem. Both functions are tested using the `doctest` module.