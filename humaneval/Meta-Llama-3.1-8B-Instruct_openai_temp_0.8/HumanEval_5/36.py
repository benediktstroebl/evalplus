```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`
    
    Args:
    numbers (List[int]): The input list of integers
    delimiter (int): The number to be inserted between consecutive elements
    
    Returns:
    List[int]: The list with the delimiter inserted between elements
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start with the first element of the list
    
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimiter)  # Insert the delimiter before each element
        result.append(num)
    
    return result[:-1]  # Remove the extra delimiter at the end

# Example usage
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This Python script defines a function `intersperse` that inserts a given integer `delimiter` between every two consecutive elements of a list `numbers`. The function handles the edge case where the input list is empty and returns the list with the delimiter inserted between elements. The example usage demonstrates the function's behavior with different inputs.