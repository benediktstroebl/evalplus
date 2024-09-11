```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between the elements
    
    Returns:
    List[int]: The list with the specified number inserted between the elements
    
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers
    
    result = [numbers[0]]
    
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])
    
    return result


# Testing the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This Python script defines the `intersperse` function as described and includes test cases to verify its functionality.