```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between consecutive elements.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This Python script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input, and returns a new list with `delimiter` inserted between every two consecutive elements of `numbers`. The function handles the edge case where `numbers` is an empty list. The example usage demonstrates the function's behavior with different inputs.