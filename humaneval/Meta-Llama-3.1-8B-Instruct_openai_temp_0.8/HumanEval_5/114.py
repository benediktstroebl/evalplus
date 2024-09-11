```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): The number to be inserted between list elements

    Returns:
        List[int]: The modified list with the delimeter inserted

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If input list is empty, return it as is
        return numbers
    result = [numbers[0]]  # Start the result with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the input list
        result.append(delimeter)  # Insert the delimeter
        result.append(num)  # Append the current number
    return result


# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([5, 10, 15, 20], 7))  # [5, 7, 10, 7, 15, 7, 20]
```