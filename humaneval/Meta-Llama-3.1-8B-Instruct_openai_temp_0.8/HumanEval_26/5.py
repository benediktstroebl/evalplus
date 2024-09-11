```markdown
### Remove Duplicates from a List

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

    Examples:
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

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

### Explanation

This script defines a function `remove_duplicates` that takes a list of integers as input, removes all elements that occur more than once, and returns the resulting list. The function uses a set `seen` to keep track of the elements it has encountered so far. It iterates over the input list and adds each element to the result list only if it has not been seen before. The function preserves the original order of the elements in the input list. The example usage at the end demonstrates how to call the function with a sample list and print the result.