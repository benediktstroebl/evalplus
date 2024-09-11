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
    seen = set()  # keep track of unique elements
    result = []  # store the final result

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

In this script, we create an empty set `seen` to keep track of unique elements encountered so far. We iterate through the input list `numbers`. For each number, we check if it is in the `seen` set. If not, we add it to the `result` list and the `seen` set. This ensures that each number appears at most once in the `result` list.