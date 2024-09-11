```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The resulting list with the delimiter inserted.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([10, 20, 30, 40], 5))  # [10, 5, 20, 5, 30, 5, 40]
```

This script defines the `intersperse` function, which takes a list of numbers and a delimiter as input. It then returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function handles the edge case where the input list is empty. The script also includes example usage to demonstrate the function's behavior.