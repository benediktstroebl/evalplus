```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The list of numbers to intersperse.
        delimiter (int): The number to insert between every two consecutive elements.

    Returns:
        List[int]: The list of numbers with the delimiter inserted between every two consecutive elements.
    """
    # Use itertools.zip_longest to pair each number with the delimiter
    pairs = itertools.zip_longest(numbers, [delimiter] * len(numbers), fillvalue=None)
    
    # Use itertools.chain to flatten the pairs into a single list
    result = list(itertools.chain(*pairs))
    
    # Remove the trailing delimiter
    if result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```