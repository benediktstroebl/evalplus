```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The modified list with delimiter inserted between consecutive elements.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which takes a list of numbers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function handles the edge case where the input list is empty, returning an empty list in this case. The test cases at the end verify the function's behavior.