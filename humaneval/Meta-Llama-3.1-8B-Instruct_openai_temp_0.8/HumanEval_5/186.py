### Interspersing Numbers in a List

This Python script defines a function `intersperse` to insert a specified number between every two consecutive elements in a given list.

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The list with the specified number inserted between elements.
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list with an index
    for i in range(len(numbers)):
        # Append the current element to the result
        result.append(numbers[i])
        
        # If it's not the last element, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the resulting list
    return result

# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script uses a simple iterative approach to generate the resulting list by appending each element from the input list and the delimiter (if not the last element) to the result list.