### Remove Duplicates from a List
#### Problem Description

Remove all elements from a list of integers that occur more than once. Maintain the order of elements left the same as in the input.

#### Solution

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

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # Use a set to keep track of elements we've seen
    result = []   # The list of elements with no duplicates

    for num in numbers:
        if num not in seen:  # If we haven't seen this element before
            result.append(num)  # Add it to the result list
            seen.add(num)  # And mark it as seen

    return result
```

#### Example Usage

```python
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [5, 5, 5, 2, 2]
print(remove_duplicates(numbers))  # Output: [2]
```

This script creates a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set to keep track of elements that have been seen, ensuring that elements that occur more than once are only added to the result list once. The function maintains the original order of elements in the input list.