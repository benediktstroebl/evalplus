```python
from typing import List
import itertools


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): Input list of integers.
    delimeter (int): Number to be inserted between consecutive elements.

    Returns:
    List[int]: Modified list with delimeter inserted.
    """
    # Use itertools.chain and itertools.cycle to create an infinite sequence of delimeter
    # then use zip_longest to pair each element in numbers with delimeter
    # then use itertools.chain.from_iterable to flatten the pairs into a single list
    result = list(itertools.chain.from_iterable(itertools.zip_longest(numbers, itertools.repeat(delimeter))))
    
    # Remove trailing delimeter if numbers is not empty
    if numbers and result[-1] is None:
        result.pop()
    
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```