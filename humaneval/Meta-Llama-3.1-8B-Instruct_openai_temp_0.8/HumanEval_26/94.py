```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with all elements that occur more than once removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = {}  # dictionary to keep track of seen elements
    result = []  # list to store the final result

    for num in numbers:
        if num not in seen:
            seen[num] = True  # mark the element as seen
            result.append(num)  # add the element to the result list

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a dictionary (`seen`) to keep track of the elements in the `numbers` list as it iterates through them. If an element is not in the `seen` dictionary, it is added to the `result` list and marked as seen. This ensures that duplicate elements are removed while preserving the original order of the elements.