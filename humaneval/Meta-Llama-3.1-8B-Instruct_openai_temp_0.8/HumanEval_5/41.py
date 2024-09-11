```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`
    
    Args:
        numbers (List[int]): The input list of numbers
        delimeter (int): The number to be inserted as a delimiter
        
    Returns:
        List[int]: The list with delimiters inserted
    
    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        if len(result) > 1:
            result.insert(-1, delimeter)
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimiter number as input and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a simple loop to append each number from the input list to the result list, and inserts the delimiter between each pair of numbers. The script also includes test cases to verify the correctness of the function.