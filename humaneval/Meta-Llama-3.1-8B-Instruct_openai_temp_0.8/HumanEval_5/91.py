```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): A list of integers.
    delimeter (int): The number to be inserted between elements.
    
    Returns:
    List[int]: The list with the delimeter inserted.
    
    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # check if the list is empty
        return []
    
    result = [numbers[0]]  # start with the first element of the list
    
    for i in range(len(numbers) - 1):  # loop through the list excluding the last element
        result.append(delimeter)  # append the delimeter
        result.append(numbers[i + 1])  # append the next element
    
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input. The function inserts the `delimeter` between every two consecutive elements of the list. It returns the resulting list. The script also includes test cases to demonstrate the function's behavior.