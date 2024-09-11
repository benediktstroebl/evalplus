```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    - numbers (List[int]): A list of integers.
    - delimiter (int): The number to be inserted between elements.

    Returns:
    - List[int]: A new list with the delimiter inserted between every two consecutive elements.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])
    return result

# Example usage
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input. It initializes an empty list `result` with the first element of `numbers`, then iterates through the rest of `numbers`, appending the delimiter and each number to `result`. If `numbers` is empty, the function returns an empty list. The script also includes example usage of the `intersperse` function.