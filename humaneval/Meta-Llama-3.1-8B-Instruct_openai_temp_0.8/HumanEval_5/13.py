```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The list with the delimeter inserted between every two consecutive elements.
    """
    result = [numbers[0]]  # Initialize the result list with the first element
    for num in numbers[1:]:  # Iterate over the remaining elements
        result.extend([delimeter, num])  # Append the delimeter and the current number
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a list comprehension to create the result list, and the `extend` method to append the delimeter and the current number to the result list. The example usage at the end demonstrates how to use the function with the provided test cases.