```python
from collections import OrderedDict
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    return [num for num, count in counts.items() if count == 1]


# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script works by first creating a dictionary (`counts`) where the keys are the numbers from the input list and the values are the counts of each number. The `OrderedDict` class is used to preserve the order in which the numbers first appear in the input list.

Then, it uses a list comprehension to create a new list that includes only the numbers that have a count of 1. This new list is returned as the result.

Please note that this solution has a time complexity of O(n), where n is the length of the input list, because it needs to iterate over the input list twice: once to count the numbers and once to create the output list. However, it only requires a single pass over the input data, making it quite efficient for large inputs.