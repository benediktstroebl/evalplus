```markdown
### Remove Duplicates from a List

This script provides a Python function to remove all elements from a list that occur more than once, preserving the original order.

#### Code
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

### Example Usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

#### Explanation

This script uses a set `seen` to keep track of numbers that have been encountered. It iterates through the input list, adding numbers to the result list only if they are not already in the `seen` set. This ensures that duplicates are removed while preserving the original order. The `seen` set is used for efficient lookups, making the solution scalable for large input lists.
```