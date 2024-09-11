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
    # Create an OrderedDict to count the occurrences of each number
    # while preserving their original order.
    counts = OrderedDict()
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Filter out numbers that occur more than once.
    unique_numbers = [num for num, count in counts.items() if count == 1]

    return unique_numbers

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise solution with a list comprehension and the `dict` constructor to create a dictionary that preserves order (only works in Python 3.7+):

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    counts = dict((num, numbers.count(num)) for num in set(numbers))
    return [num for num in numbers if counts[num] == 1]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```