```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Don't append delimiter after last element
            result.append(delimiter)
    return result

# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function iterates over the input list, appending each element and the delimiter (if it's not the last element) to the result list.

The script also includes two test cases using the `assert` statement to verify that the function works as expected.