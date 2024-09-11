```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The modified list with the delimeter inserted between elements.

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # check if the list is empty
        return []
    
    result = [numbers[0]]  # start with the first number
    for num in numbers[1:]:  # loop through the rest of the numbers
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number
    
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a number as input, and returns a new list where the input number is inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to construct the result list. The example use cases are included at the end to demonstrate the function's behavior.