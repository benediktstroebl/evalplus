```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): The number to be inserted between elements of the list

    Returns:
        List[int]: The modified list with delimeter inserted between elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.extend([delimeter, num])  # Insert the delimeter and then the number
    return result

# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It then inserts the delimiter between every two consecutive elements of the list and returns the modified list. The function handles the case where the input list is empty by returning it as is. The script also includes test cases to verify the correctness of the function.