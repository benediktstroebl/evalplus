```markdown
### Problem: Remove Duplicates from List

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
    seen = set()
    result = [num for num in numbers if not (num in seen or seen.add(num))]
    return result
```

#### Explanation

This solution uses a list comprehension to create a new list with duplicates removed. It keeps track of the numbers it has seen using a `set`, which allows for efficient lookups.

The `or seen.add(num)` expression is a clever trick. If `num` is already in `seen`, `seen.add(num)` will do nothing, so the expression will be `False`, and `num` will be included in the result. If `num` is not in `seen`, `seen.add(num)` will add it to `seen`, so the expression will be `True`, and `num` will be excluded from the result.

This solution has a time complexity of O(n), where n is the length of the input list, because each number is added to the `seen` set at most once. The space complexity is also O(n), because in the worst case, all numbers are unique, and the `seen` set will contain all of them.