```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the elements of the input list.
    
    Returns:
    List[int]: The list with the delimeter inserted between every two consecutive elements.
    """
    if not numbers:  # If the input list is empty, return the empty list.
        return []
    
    result = [numbers[0]]  # Start the result list with the first element of the input list.
    
    for num in numbers[1:]:  # Iterate over the rest of the elements in the input list.
        result.append(delimeter)  # Insert the delimeter between each pair of elements.
        result.append(num)
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines the `intersperse` function as per the provided specification. It iterates over the input list, inserting the delimeter between each pair of elements and returning the resulting list. The test cases are included at the end to demonstrate the function's behavior.