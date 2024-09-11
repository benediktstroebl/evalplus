```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: A list of integers.
        delimiter: The number to be inserted between consecutive elements.

    Returns:
        A new list with 'delimiter' inserted between every two consecutive elements of `numbers`.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimiter)
        result.append(num)

    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter integer as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to construct the new list. The script also includes two test cases to demonstrate the function's behavior.