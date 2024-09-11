```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of numbers
        delimeter (int): The number to insert between elements
    
    Returns:
        List[int]: The modified list with delimeter inserted
    
    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the extra delimeter at the end
    result.pop()
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input. It iterates over the input list, appending each number and the delimeter to the result list. After the loop, it removes the extra delimeter at the end of the result list. The script then includes test cases to demonstrate the function's behavior.