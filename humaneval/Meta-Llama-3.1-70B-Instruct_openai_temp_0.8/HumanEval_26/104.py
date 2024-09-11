```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an OrderedDict to maintain the order of elements
    count_map = OrderedDict()
    
    # Count the occurrence of each number
    for num in numbers:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    # Filter out numbers that occur more than once
    result = [num for num, count in count_map.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses an `OrderedDict` to count the occurrence of each number in the input list while maintaining the original order. It then uses a list comprehension to filter out numbers that occur more than once. The result is a list of numbers that occur only once, in the same order as they appear in the input list.