```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between consecutive elements.
    
    Returns:
    List[int]: The list with the delimeter inserted between consecutive elements.
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        
        # If it's not the last number, add the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    # Return the result list
    return result

# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to build the result list. The test cases at the end demonstrate the function's behavior with different inputs.