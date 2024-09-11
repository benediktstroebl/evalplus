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
    # Create an OrderedDict to keep track of the elements we've seen and their counts
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    # Filter out elements that occur more than once
    result = [num for num, count in counts.items() if count == 1]

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
Alternatively, you can use a single dictionary to keep track of counts and a list comprehension to filter out duplicates. Here is an example:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return [num for num in numbers if counts[num] == 1]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```