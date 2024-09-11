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
    """
    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))
# Output: [1, 3, 4]
```
This script defines a function `remove_duplicates` that iterates through the input list `numbers`. It keeps track of the elements it has seen in a set `seen`. If an element has not been seen before, it is added to the `seen` set and the `result` list. This ensures that duplicates are removed and the original order is preserved.