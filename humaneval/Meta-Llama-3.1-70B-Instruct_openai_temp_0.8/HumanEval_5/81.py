```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers and a delimiter as input. It iterates over the input list, appending each number to the result list, and also appends the delimiter after each number except the last one. The function then returns the modified list.