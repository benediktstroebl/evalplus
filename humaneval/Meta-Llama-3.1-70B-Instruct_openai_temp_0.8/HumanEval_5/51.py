```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The modified list with the delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases:
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input, and returns a new list where the delimeter is inserted between every two consecutive elements. The `enumerate` function is used to keep track of the index of the current element, so that we can append the delimeter only if it's not the last element in the list. The test cases at the end verify that the function works correctly.