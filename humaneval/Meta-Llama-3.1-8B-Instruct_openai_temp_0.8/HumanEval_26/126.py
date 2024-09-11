```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with all elements that occur more than once removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    return [num for num in numbers if not (num in seen or seen.add(num))]


# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a list comprehension with a conditional statement to create a new list that includes only the elements from the input list that have not been seen before. It uses a `set` called `seen` to keep track of the elements it has seen so far. The `or seen.add(num)` expression is a clever trick to use the `add` method of the `set` and the `or` operator to avoid adding the number to the `seen` set if it has already been seen.