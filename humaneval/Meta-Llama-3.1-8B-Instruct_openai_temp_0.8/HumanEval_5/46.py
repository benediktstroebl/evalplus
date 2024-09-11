```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted between every two consecutive elements.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty
        return []

    result = [numbers[0]]  # start with the first element of the list
    for num in numbers[1:]:  # iterate over the rest of the list
        result.extend([delimeter, num])  # add the delimeter and the current number to the result list
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```