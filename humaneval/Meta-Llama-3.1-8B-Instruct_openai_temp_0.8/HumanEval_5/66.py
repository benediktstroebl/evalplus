```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): Input list of integers
        delimiter (int): Number to be inserted between elements

    Returns:
        List[int]: List of integers with 'delimiter' inserted between every two elements
    """
    if not numbers:  # Base case: If the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimiter)  # Insert the delimiter
        result.append(num)  # Add the current number
    return result

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script uses a simple iterative approach to solve the problem. It checks for the base case of an empty list and handles it separately. For non-empty lists, it starts with the first element, inserts the delimiter and the current number in each iteration, resulting in the desired output.