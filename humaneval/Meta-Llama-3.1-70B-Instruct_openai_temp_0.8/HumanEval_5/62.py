```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers
        delimiter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The resulting list with the delimiter inserted
    """
    return list(itertools.chain.from_iterable(
        [num, delimiter] if i < len(numbers) - 1 else [num]
        for i, num in enumerate(numbers)
    ))

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

In this code:

*   We use the `itertools.chain.from_iterable` function to flatten a list of lists into a single list.
*   We use a generator expression to create a list of lists where each inner list contains a number from the input list and the delimiter (unless it's the last number in the list).