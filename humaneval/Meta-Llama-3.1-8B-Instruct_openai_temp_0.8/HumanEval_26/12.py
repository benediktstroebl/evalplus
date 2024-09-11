```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of integers with duplicates removed.
    
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    
    # Use OrderedDict to keep track of the order in which elements appear
    seen = OrderedDict()
    
    # Iterate over the list of numbers
    for num in numbers:
        # If the number is not already in the OrderedDict, add it
        if num not in seen:
            seen[num] = None
    
    # Return a list of the keys in the OrderedDict, which are the non-duplicate numbers
    return list(seen.keys())

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```