```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It initializes the result list with the first number from the input list, then iterates over the remaining numbers, appending the delimiter and each number to the result list. Finally, it returns the modified list.

The test cases at the end of the script demonstrate the function's behavior with an empty list and a list of numbers.