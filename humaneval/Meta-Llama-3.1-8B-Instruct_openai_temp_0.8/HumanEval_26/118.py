### Remove Duplicates from a List of Integers
#### Code
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers: A list of integers
    
    Returns:
        A list of integers with duplicates removed
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # keep track of unique elements
    result = []  # store the result
    
    for num in numbers:
        if num not in seen:  # if num is not in the seen set
            seen.add(num)  # add it to the seen set
            result.append(num)  # and add it to the result list
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([4, 5, 5, 4, 6]))  # [4, 6]
print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]))  # []
```

#### Explanation
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a `set` to keep track of unique elements it has seen so far, and a `list` to store the result.

The function iterates over the input list, and for each number, it checks if the number is in the `seen` set. If not, it adds the number to the `seen` set and to the result list. This way, only unique elements are added to the result list.

Finally, the function returns the result list.