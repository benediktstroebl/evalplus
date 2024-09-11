```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The integer to be inserted between consecutive elements

    Returns:
    List[int]: The list with delimeter inserted between every two consecutive elements
    """
    if not numbers:  # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start the result with the first element of the input list
    
    for i in range(1, len(numbers)):  # Iterate over the rest of the elements
        result.append(delimeter)  # Insert the delimeter
        result.append(numbers[i])  # Append the current element
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([5, 6, 7], 8))  # [5, 8, 6, 8, 7]
print(intersperse([9], 10))  # [9]
```

This script defines a function `intersperse` that takes a list of integers and an integer as input, and returns a new list with the delimeter inserted between every two consecutive elements of the input list. It uses a simple iterative approach to build the result list, starting with the first element of the input list and appending the delimeter and the current element at each step. The function also handles the edge case where the input list is empty. The test cases demonstrate the function's behavior with different inputs.