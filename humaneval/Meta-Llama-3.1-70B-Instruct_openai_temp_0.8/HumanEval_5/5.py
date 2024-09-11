```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): A list of integers
        delimiter (int): The number to be inserted between the elements of the input list

    Returns:
        List[int]: The modified list with the delimiter inserted between every two consecutive elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result

# Test cases
assert intersperse([], 4) == []  # Output: []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]  # Output: [1, 4, 2, 4, 3]
assert intersperse([-1, 0, 1], 5) == [-1, 5, 0, 5, 1]  # Output: [-1, 5, 0, 5, 1]
assert intersperse([10, 20, 30, 40, 50], 0) == [10, 0, 20, 0, 30, 0, 40, 0, 50]  # Output: [10, 0, 20, 0, 30, 0, 40, 0, 50]
```

This Python script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input. It returns a new list where the `delimiter` is inserted between every two consecutive elements of the input list. The function uses a for loop to iterate over the input list, appending each element and the delimiter (if it's not the last element) to the result list. The script includes several test cases to demonstrate the function's correctness.