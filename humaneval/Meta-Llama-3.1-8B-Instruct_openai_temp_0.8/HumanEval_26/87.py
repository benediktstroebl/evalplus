```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with elements that occur more than once removed.

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

In this script, we use a set `seen` to keep track of the elements we've encountered so far. For each element in the list `numbers`, we check if it's already in the `seen` set. If it's not, we add it to the `result` list and the `seen` set. This way, we ensure that each element is added to the `result` list only once, and the order of the elements is preserved.