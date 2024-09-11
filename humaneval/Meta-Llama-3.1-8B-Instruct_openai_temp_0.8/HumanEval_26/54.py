```markdown
### Remove Duplicates from a List

This script provides a function `remove_duplicates` to remove all elements that occur more than once from a given list of integers, preserving the original order.

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

In this script, we use a set `seen` to keep track of the numbers we've seen so far. We iterate over the list `numbers`, and for each number, we check if it's in the `seen` set. If it's not, we add it to the `seen` set and append it to the `result` list. This way, we ensure that each number appears in the `result` list only once, and the original order is preserved.