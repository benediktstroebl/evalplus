```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between the elements.

    Returns:
        List[int]: The list with the specified delimeter inserted between the elements.
    """
    result = []
    for n in numbers:
        result.append(n)
        result.append(delimeter)
    # Remove the last occurrence of the delimeter
    if len(result) > 1:
        result.pop()
    return result

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers and a delimeter integer as input and returns a new list with the specified delimeter inserted between the elements. The test cases demonstrate the function's behavior with an empty list and a list with three elements.