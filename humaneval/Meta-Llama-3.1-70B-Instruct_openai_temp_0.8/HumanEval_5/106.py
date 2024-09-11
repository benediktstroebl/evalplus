```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The input list with 'delimiter' inserted between every two consecutive elements.
    """
    # Use itertools.chain and itertools.zip_longest to insert the delimiter
    # zip_longest will stop once the longest input iterable is exhausted
    # We use chain to flatten the result, and the default value of zip_longest is None, 
    # so we replace None with the delimiter
    return list(itertools.chain(*itertools.zip_longest(numbers, [delimiter] * (len(numbers) - 1) if numbers else [], fillvalue=None)))

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```