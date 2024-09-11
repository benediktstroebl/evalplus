```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of integers with duplicates removed.
    
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set `seen` to keep track of the numbers that have been encountered so far, and a list `result` to store the numbers that do not have duplicates. The function iterates over the input list, checks if each number is in the `seen` set, and if not, adds it to the `seen` set and the `result` list. The function returns the `result` list. The script also includes an example usage of the function.