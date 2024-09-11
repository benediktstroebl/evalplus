```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Only append the delimiter if it's not the last element
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which iterates over the input list `numbers`. For each number, it appends the number to the result list and then checks if it's not the last element in the list. If it's not the last element, it appends the `delimiter` to the result list. The function then returns the resulting list.

The script also includes two test cases to demonstrate the function's behavior.