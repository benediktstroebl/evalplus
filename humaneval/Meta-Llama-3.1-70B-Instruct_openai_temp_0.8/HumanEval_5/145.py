```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([10, 20, 30, 40], 5))  # [10, 5, 20, 5, 30, 5, 40]
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a for loop to iterate over the input list, and checks if it's not the last element before appending the delimiter. The test cases at the end demonstrate the function's behavior.