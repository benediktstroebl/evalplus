```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    
    Args:
        numbers (List[int]): The list of integers to be modified.
        delimeter (int): The number to be inserted between the elements.
    
    Returns:
        List[int]: The modified list with the delimeter inserted.
    
    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    return result


# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as arguments. It returns a new list where the `delimeter` is inserted between every two consecutive elements of the input list. The function first handles the edge case where the input list is empty, and then inserts the `delimeter` between the elements using a loop. The script also includes test cases to demonstrate the function's behavior.