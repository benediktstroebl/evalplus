```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    seen = OrderedDict()
    for num in numbers:
        seen[num] = None  # add to OrderedDict to preserve order and remove duplicates
    return list(seen.keys())

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 2, 3, 4]
print(remove_duplicates([5, 5, 5, 5]))  # Expected output: [5]
print(remove_duplicates([1, 2, 3, 4, 5]))  # Expected output: [1, 2, 3, 4, 5]
print(remove_duplicates([]))  # Expected output: []
```