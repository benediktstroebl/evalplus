```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): The list of numbers to intersperse.
        delimiter (int): The number to insert between every two consecutive elements.

    Returns:
        List[int]: The list with 'delimiter' inserted between every two consecutive elements.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result


# Example use cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that inserts a specified delimiter between every two consecutive elements of a given list of numbers. The function returns a new list with the delimiter inserted. The script also includes example use cases to demonstrate the function's behavior.