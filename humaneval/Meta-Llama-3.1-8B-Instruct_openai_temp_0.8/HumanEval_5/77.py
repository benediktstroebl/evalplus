```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`
    
    Args:
    numbers (List[int]): Input list of integers
    delimeter (int): Number to insert between elements
    
    Returns:
    List[int]: List with delimeter inserted between elements
    
    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    
    if not numbers:  # if input list is empty
        return []
    
    result = [numbers[0]]  # start with the first element
    
    for i in range(1, len(numbers)):  # iterate through the rest of the list
        result.extend([delimeter, numbers[i]])  # insert delimeter and current element
        
    return result

# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers and a number to insert between elements as input, and returns a new list with the specified number inserted between elements. If the input list is empty, it returns an empty list. The function uses a simple loop to iterate through the input list, inserting the delimeter and current element into the result list at each iteration. The script also includes test cases to demonstrate the function's behavior.