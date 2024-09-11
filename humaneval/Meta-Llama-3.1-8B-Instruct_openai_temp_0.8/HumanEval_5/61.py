```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integer numbers.
        delimeter (int): The integer number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted between every two consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # Check if the input list is empty
        return []
    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.extend([delimeter, num])  # Insert the delimeter and the current number
    return result

# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This Python script solves the given problem by creating a function `intersperse` that takes a list of integers and an integer delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to achieve this.