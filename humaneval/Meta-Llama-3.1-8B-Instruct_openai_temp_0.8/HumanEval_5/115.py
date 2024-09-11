```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between elements

    Returns:
    List[int]: The modified list with delimeter inserted

    Example:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers
    result = [numbers[0]]  # Start the result with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter before the current number
        result.append(num)  # Append the current number
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimeter as input. It returns a new list with the delimeter inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to build the result list. If the input list is empty, it returns the empty list. The provided test cases demonstrate the function's behavior.