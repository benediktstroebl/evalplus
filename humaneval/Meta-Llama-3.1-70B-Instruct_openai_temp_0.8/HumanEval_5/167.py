```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The list with the delimiter inserted between every two consecutive elements.
    """
    # If the input list is empty, return an empty list
    if not numbers:
        return []

    # Use itertools.zip_longest to pair each number with the delimiter
    # The * operator is used to unpack the list into separate arguments
    paired = itertools.zip_longest(numbers, numbers[1:], fillvalue=delimiter)

    # Chain the paired numbers and delimiters together into a single list
    # The * operator is used to unpack the tuples into separate arguments
    result = [item for pair in paired for item in pair]

    return result


# Test cases
assert intersperse([], 4) == []
assert intersperse([1], 4) == [1]
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
assert intersperse([1, 2, 3, 4], 5) == [1, 5, 2, 5, 3, 5, 4]
```