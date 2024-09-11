```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between elements.

    Returns:
        List[int]: The list with 'delimiter' inserted between every two consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    # Use itertools.zip_longest to pair each element with the delimiter
    paired = itertools.zip_longest(numbers, numbers[1:], fillvalue=None)
    # Use itertools.chain to flatten the pairs and remove the None values
    return [x for pair in paired for x in pair if x is not None]

# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
```