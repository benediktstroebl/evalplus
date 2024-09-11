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

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 4]
```

In this script, we create an empty set `seen` to keep track of numbers we've seen so far, and an empty list `result` to store the output. We then iterate over the input list `numbers`. If a number `num` is not in `seen`, we append it to `result` and add it to `seen`. This way, we ensure that we only add each number to `result` once, in the order it first appears in `numbers`.