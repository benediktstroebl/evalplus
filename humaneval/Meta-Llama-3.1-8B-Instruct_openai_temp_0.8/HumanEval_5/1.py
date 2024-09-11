Here's the self-contained Python script that solves the problem:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        # If input list is empty, return empty list
        return []
    
    result = [numbers[0]]
    
    for i in range(1, len(numbers)):
        # Append delimiter and number
        result.extend([delimiter, numbers[i]])
    
    return result

# Example usage:
print(intersperse([], 4))   # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This Python script implements the `intersperse` function as specified. The time complexity is O(n), where n is the number of elements in the input list.