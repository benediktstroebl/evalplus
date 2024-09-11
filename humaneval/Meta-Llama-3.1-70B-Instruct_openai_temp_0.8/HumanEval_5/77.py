```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a for loop to iterate over the input list and appends the delimiter before each element except the first one. The modified list is then returned as the result.

The script also includes test cases to demonstrate the usage and correctness of the `intersperse` function. The test cases cover the edge case of an empty input list and a non-empty input list with multiple elements.