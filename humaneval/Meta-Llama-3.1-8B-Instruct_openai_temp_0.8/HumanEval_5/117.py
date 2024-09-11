```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The modified list with 'delimeter' inserted between elements.

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # Return empty list if input list is empty

    result = [numbers[0]]  # Start with the first element
    for i in range(1, len(numbers)):
        result.append(delimeter)  # Insert delimeter before current element
        result.append(numbers[i])  # Append the current element

    return result


# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that inserts a specified number `delimeter` between every two consecutive elements of the input list `numbers`. The function uses a simple loop to append the delimeter before each element in the list, effectively interspersing the delimeter between elements. The script also includes test cases to demonstrate the function's behavior.