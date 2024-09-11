```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result


# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
print("All test cases pass")
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It then iterates over the input list, appending the delimiter before each number except the first one. The function returns the resulting list.

The script also includes two test cases to verify the correctness of the `intersperse` function. If the function works correctly, it prints "All test cases pass".