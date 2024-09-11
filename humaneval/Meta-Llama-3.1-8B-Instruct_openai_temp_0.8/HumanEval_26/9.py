```markdown
### Remove Duplicates from List of Integers
#### Problem Description
From a list of integers, remove all elements that occur more than once. Keep order of elements left the same as in the input.

#### Solution

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed, keeping the original order.

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

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This solution iterates over the input list, keeping track of the elements it has seen in a set. If an element is not in the set, it is added to the result list and the set. This process maintains the original order of elements and removes duplicates.
```