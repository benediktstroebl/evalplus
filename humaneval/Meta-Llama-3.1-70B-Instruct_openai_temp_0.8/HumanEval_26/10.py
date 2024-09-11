```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed.
    """
    # Create an OrderedDict to keep track of element counts
    counts = OrderedDict()
    for num in numbers:
        # If the number is already in the OrderedDict, increment its count
        if num in counts:
            counts[num] += 1
        # If the number is not in the OrderedDict, add it with a count of 1
        else:
            counts[num] = 1

    # Use a list comprehension to create the result list
    # Only include numbers with a count of 1
    return [num for num, count in counts.items() if count == 1]


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```