```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers

    Returns:
        A list of integers with duplicates removed
    """
    # Count the occurrences of each number using OrderedDict to preserve order
    counts = OrderedDict()
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Filter out numbers that occur more than once
    return [num for num, count in counts.items() if count == 1]


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```
This script defines a function `remove_duplicates` that removes duplicates from a list of integers while preserving the original order. It uses an `OrderedDict` to count the occurrences of each number, then filters out numbers that occur more than once. The test case at the end verifies that the function works as expected.