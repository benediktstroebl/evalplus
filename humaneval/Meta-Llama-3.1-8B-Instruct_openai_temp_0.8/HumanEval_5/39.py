```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.
        
    Returns:
        List[int]: The list with the delimiter inserted between every two consecutive elements.
        
    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the input list is empty, return the empty list.
        return []
    
    result = [numbers[0]]  # Start the result list with the first element of the input list.
    
    for num in numbers[1:]:  # Iterate over the rest of the elements in the input list.
        result.append(delimiter)  # Insert the delimiter in the result list.
        result.append(num)  # Append the current element to the result list.
        
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```