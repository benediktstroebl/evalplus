```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an ordered dictionary to keep track of element counts
    counts = OrderedDict()
    
    # Count the occurrences of each element
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Return a list of elements that occur only once
    return [num for num, count in counts.items() if count == 1]

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the elements that occur once in the input list, in their original order. It uses an `OrderedDict` to count the occurrences of each element, and a list comprehension to create the output list. The script also includes an example usage of the function.