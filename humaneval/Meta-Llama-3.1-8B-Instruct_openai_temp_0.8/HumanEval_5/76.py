```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.
        
    Returns:
        List[int]: The modified list with the delimeter inserted between elements.
    
    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # Check if the list is empty
        return numbers  # Return an empty list immediately
    
    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter
        result.append(num)  # Insert the current number
    
    return result  # Return the modified list


# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers and a number as input, and returns a new list with the number inserted between every two consecutive elements. The function uses a simple iterative approach to build the modified list. The script also includes doctests to verify its correctness.