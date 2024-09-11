```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.
    
    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: The list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that inserts a specified delimiter between every two consecutive elements of a given list of numbers. The function iterates over the input list, appending the delimiter before each number except the first one. The result is a new list with the delimiter inserted between every two consecutive elements.