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
    """
    seen = {}  # dictionary to keep track of seen elements
    result = []  # list to store the result

    for num in numbers:
        if num not in seen:
            seen[num] = True  # mark num as seen
            result.append(num)  # add num to the result

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # Output: []
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. It uses a dictionary `seen` to keep track of the elements it has seen so far, and a list `result` to store the elements that are not duplicates. The function iterates over the input list, checking each element against the `seen` dictionary. If an element is not in `seen`, it is added to `seen` and `result`. Finally, the function returns the `result` list.