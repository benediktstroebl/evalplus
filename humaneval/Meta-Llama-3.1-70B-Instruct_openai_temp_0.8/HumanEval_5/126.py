```python
from typing import List
import itertools


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): Input list of integers.
    delimiter (int): Delimiter to be inserted between consecutive elements.

    Returns:
    List[int]: List with delimiter inserted between consecutive elements.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    return list(itertools.chain.from_iterable(
        [x, delimiter] if i < len(numbers) - 1 else [x]
        for i, x in enumerate(numbers)
    ))


if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as required. The function uses the `itertools.chain.from_iterable` function to create an iterator that inserts the `delimiter` between consecutive elements of the `numbers` list. The `if __name__ == "__main__":` block is used to test the function with the provided examples.