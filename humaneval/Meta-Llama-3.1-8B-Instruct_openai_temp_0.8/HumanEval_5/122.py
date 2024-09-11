```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list `numbers`
    
    Args:
    numbers (List[int]): The input list of integers
    delimiter (int): The number to insert between consecutive elements
    
    Returns:
    List[int]: The list with the delimiter inserted between consecutive elements
    
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the input list is empty, return it immediately
        return numbers
    
    result = [numbers[0]]  # Start with the first element of the input list
    
    for i in range(1, len(numbers)):  # Iterate over the rest of the list
        result.append(delimiter)  # Insert the delimiter
        result.append(numbers[i])  # Append the current element
    
    return result


# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this script, we define a function `intersperse` that takes a list of integers and an integer delimiter as input. It checks if the input list is empty, and if so, returns it immediately. Otherwise, it creates a new list with the first element of the input list, then iterates over the rest of the list, inserting the delimiter and the current element at each step. Finally, the function returns the modified list.