```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): Number to be inserted between every two consecutive elements

    Returns:
        List[int]: List with the specified delimeter inserted between every two consecutive elements

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # If input list is empty, return it as is

    result = [numbers[0]]  # Start the result list with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the input list
        result.append(delimeter)  # Add the delimeter to the result list
        result.append(num)  # Add the current number to the result list
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4], 5))  # [1, 5, 2, 5, 3, 5, 4]
```