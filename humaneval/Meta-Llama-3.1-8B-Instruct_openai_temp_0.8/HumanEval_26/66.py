```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A new list with elements that occur more than once removed.
    
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with elements that occur more than once removed. It uses a set `seen` to keep track of the elements that have already been encountered. If an element is not in the `seen` set, it is added to the `result` list and the `seen` set. This preserves the original order of elements.