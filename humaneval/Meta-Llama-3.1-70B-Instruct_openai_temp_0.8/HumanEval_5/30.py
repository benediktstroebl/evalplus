```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between elements.

    Returns:
    List[int]: The modified list with 'delimiter' inserted between every two elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Insert delimiter after each element except the last one
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example use cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimiter as input. It iterates over the input list, appending each element to the result list, and then checks if it's not the last element in the list. If it's not the last element, it appends the delimiter to the result list. Finally, it returns the modified list.