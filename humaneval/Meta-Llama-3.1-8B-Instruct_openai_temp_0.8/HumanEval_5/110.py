```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to insert between the list elements.

    Returns:
        List[int]: The list with the delimeter inserted between elements.
    """
    if not numbers:
        # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]
    # Start from the second element of the list
    for num in numbers[1:]:
        # Append the delimeter and then the current number to the result list
        result.extend([delimeter, num])
    
    # Remove the last occurrence of the delimeter
    if result and result[-1] == delimeter:
        result.pop()
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers and a delimeter integer as input, and returns a new list where the delimeter is inserted between every two consecutive elements of the input list. The function handles the edge case where the input list is empty and also removes the extra delimeter at the end if present. The test cases provided in the docstring are executed at the end of the script to verify its correctness.