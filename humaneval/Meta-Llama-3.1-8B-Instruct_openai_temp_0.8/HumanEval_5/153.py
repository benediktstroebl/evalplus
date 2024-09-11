### Interspersed List Function
```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): A list of integers
    delimiter (int): An integer to be inserted between every two consecutive elements
    
    Returns:
    List[int]: The interspersed list
    
    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list, inserting the delimiter in between
    for i in range(len(numbers)):
        # Append the current number to the result
        result.append(numbers[i])
        
        # If it's not the last number, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the interspersed list
    return result


# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and an integer delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to construct the result list.