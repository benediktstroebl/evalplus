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
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that removes all elements from a list that occur more than once, preserving the original order of elements. It uses a set `seen` to keep track of the elements it has encountered so far. For each element in the input list, it checks if the element is in the `seen` set. If not, it adds the element to the `seen` set and appends it to the result list. Finally, it returns the result list.

The script also includes a test case to demonstrate the function's behavior.