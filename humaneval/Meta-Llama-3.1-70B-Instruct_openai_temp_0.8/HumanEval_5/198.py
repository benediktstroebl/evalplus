```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between consecutive elements.
    
    Returns:
    List[int]: A new list with the delimiter inserted between consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result


# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

# Example usage:
numbers = [1, 2, 3, 4, 5]
delimiter = 0
print(intersperse(numbers, delimiter))  # Output: [1, 0, 2, 0, 3, 0, 4, 0, 5]
```