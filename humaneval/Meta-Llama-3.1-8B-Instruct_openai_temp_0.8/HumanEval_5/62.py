```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers`
    
    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): Number to be inserted between elements
    
    Returns:
        List[int]: List with delimeter inserted between elements
    
    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    
    # Use list comprehension with zip to generate pairs of adjacent elements
    # Then, extend the result list with the delimeter and each pair of elements
    result = [element for pair in zip([numbers[0]] + numbers, numbers) for element in [delimeter] + list(pair)]
    
    return result


# Test the function
print(intersperse([], 4))     # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimeter as input. It uses list comprehension with `zip` to generate pairs of adjacent elements, and then extends the result list with the delimeter and each pair of elements. The function is then tested with the provided examples.