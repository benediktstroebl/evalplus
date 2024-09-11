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

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # Initialize an empty list to store the result
    result = []

    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        
        # If it's not the last number in the list, add the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)

    return result


# Test cases
print(intersperse([], 4))  # Expected: []
print(intersperse([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # Expected: [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This Python script defines a function `intersperse` that takes a list of integers and a delimiter as input. It then inserts the delimiter between every two consecutive elements in the list. The function returns a new list with the delimiter inserted. The script also includes test cases to verify the function's correctness.