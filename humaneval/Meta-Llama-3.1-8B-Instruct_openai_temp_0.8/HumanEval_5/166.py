```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between list elements

    Returns:
    List[int]: The list with the delimeter inserted between elements
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the input list with an index
    for i, num in enumerate(numbers):
        # Append the current number to the result list
        result.append(num)
        
        # If it's not the last element in the list, append the delimeter
        if i!= len(numbers) - 1:
            result.append(delimeter)
    
    # Return the result list
    return result

# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer as input, and returns a new list with the integer delimeter inserted between every two consecutive elements of the input list. The function works by iterating through the input list and appending the current number and the delimeter to the result list. If it's not the last element in the list, it appends the delimeter. Finally, the function returns the result list. The script includes example use cases to test the function.