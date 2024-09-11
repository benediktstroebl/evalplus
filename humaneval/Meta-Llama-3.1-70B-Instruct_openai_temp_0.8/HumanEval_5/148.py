```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers: A list of integers.
        delimiter: The number to be inserted between every two consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list using the itertools.zip_longest function to pair each element with the next one
    it = iter(numbers)
    for x in it:
        result.append(x)
        try:
            next(it)
        except StopIteration:
            break
        result.append(delimiter)
    
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```