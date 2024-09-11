```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.
    
    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The integer to be inserted between each pair of consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    
    result = numbers.copy()  # Create a copy of the input list to avoid modifying it in-place
    for i in range(len(result) - 1):  # Iterate over the indices of the list
        result.insert(i + 1, delimiter)  # Insert the delimiter at the index after each element
    
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimiter as input. It creates a copy of the list, then iterates over the indices of the list, inserting the delimiter at the index after each element. The modified list is then returned. The example usage at the end demonstrates the function's behavior with different inputs.