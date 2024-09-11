```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The list with the delimeter inserted between elements
    """
    result = []
    for i, num in enumerate(numbers):
        # Append the number at the current index
        result.append(num)
        # If it's not the last number, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input, and returns a new list where the `delimeter` is inserted between every two consecutive elements of `numbers`. The function uses a simple loop to iterate over the input list and append each number to the result list, followed by the delimiter if it's not the last number. The script also includes test cases to demonstrate the function's behavior.