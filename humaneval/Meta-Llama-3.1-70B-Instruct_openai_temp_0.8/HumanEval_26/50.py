```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Use OrderedDict to keep track of element counts while preserving order
    element_counts = OrderedDict()
    for num in numbers:
        element_counts[num] = element_counts.get(num, 0) + 1

    # Filter out elements with count more than 1
    result = [num for num, count in element_counts.items() if count == 1]

    return result


# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```