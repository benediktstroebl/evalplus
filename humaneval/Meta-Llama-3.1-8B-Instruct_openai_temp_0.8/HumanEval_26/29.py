```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of integers with no duplicates.
    """
    # Use an OrderedDict to preserve the order of elements and remove duplicates
    seen = OrderedDict()
    for num in numbers:
        seen[num] = None
    
    # Convert the OrderedDict keys back to a list and return
    return list(seen.keys())

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
print(remove_duplicates([4, 5, 5, 4]))  # Output: [4, 5]
```

This script defines a function `remove_duplicates` that takes a list of integers as input, removes duplicates while preserving the order of elements, and returns the resulting list. It uses an `OrderedDict` to keep track of the elements it has seen so far and to remove duplicates. The keys of the `OrderedDict` are the unique elements in the input list, and the values are irrelevant. The function converts the `OrderedDict` keys back to a list and returns it. The script also includes test cases to demonstrate the function's behavior.