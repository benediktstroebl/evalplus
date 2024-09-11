```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert as a delimiter

    Returns:
        List[int]: The modified list with the delimiter inserted
    """
    if not numbers:  # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Initialize the result list with the first element
    for num in numbers[1:]:  # Iterate over the rest of the elements in the input list
        result.extend([delimeter, num])  # Append the delimiter and the current number to the result list
    return result


# Example use cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This Python script defines a function `intersperse` that inserts a specified delimiter between every two consecutive elements of an input list of integers. The function handles the edge case where the input list is empty and returns it as is. The example use cases demonstrate the function's behavior with different inputs.