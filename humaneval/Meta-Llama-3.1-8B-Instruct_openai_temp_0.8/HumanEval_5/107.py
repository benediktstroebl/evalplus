```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimiter (int): The number to be inserted between elements

    Returns:
    List[int]: The modified list with the delimiter inserted
    """
    if not numbers:  # Base case: If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start the result list with the first element of the input list
    
    for i in range(1, len(numbers)):  # Iterate over the rest of the input list
        result.append(delimiter)  # Insert the delimiter before each element
        result.append(numbers[i])  # Append the current element
    
    return result

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. It uses a recursive approach to handle the base case (an empty input list) and the general case (a non-empty input list). The function includes docstrings to provide documentation and comments to explain the code. The test cases demonstrate how the function works.