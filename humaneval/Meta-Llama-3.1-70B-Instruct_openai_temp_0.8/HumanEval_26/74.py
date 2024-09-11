```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Count occurrences of each number
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    # Filter out numbers that occur more than once
    unique_numbers = [num for num, count in counts.items() if count == 1]

    return unique_numbers


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

This script works by first counting the occurrences of each number in the input list using an `OrderedDict`, which preserves the order of elements. It then uses a list comprehension to filter out the numbers that occur more than once, returning a list of unique numbers in the original order.