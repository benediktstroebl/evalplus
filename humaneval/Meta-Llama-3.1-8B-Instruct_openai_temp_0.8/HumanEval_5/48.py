```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between elements.

    Returns:
    List[int]: The modified list with the delimeter inserted.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty, return the empty list
        return []
    
    result = [numbers[0]]  # start with the first element
    for num in numbers[1:]:  # iterate over the rest of the list
        result.extend([delimeter, num])  # insert the delimeter and the current number
    return result

# Example usage:
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script uses the `extend` method to add elements to the end of the `result` list. It starts with the first element of the `numbers` list, then for each subsequent element, it appends the delimeter and the current number to the result. This ensures that the delimeter is inserted between every two consecutive elements of the input list.