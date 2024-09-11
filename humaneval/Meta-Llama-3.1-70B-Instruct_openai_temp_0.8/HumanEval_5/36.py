```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The modified list with delimeter inserted
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a for loop to iterate over the input list, appending each number and the delimeter (if applicable) to the result list. The function includes type hints and docstrings for clarity and readability.