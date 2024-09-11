```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The modified list with the delimeter inserted between elements
    """
    # Initialize an empty list to store the result
    result = []

    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Append the current number to the result
        result.append(num)

        # If we're not at the last number in the list, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)

    # Return the modified list
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script uses a for loop to iterate over the input list. In each iteration, it appends the current number to the result list, and also appends the delimeter after the current number, unless it's the last number in the list. This way, the delimeter is inserted between every two consecutive elements of the input list.