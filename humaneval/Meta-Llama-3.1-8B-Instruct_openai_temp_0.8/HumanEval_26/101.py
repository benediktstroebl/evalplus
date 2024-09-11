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
    seen = {}  # dictionary to keep track of numbers we've seen before
    result = []  # list to store the final result

    for num in numbers:
        if num not in seen:  # if we haven't seen this number before
            seen[num] = True  # mark it as seen
            result.append(num)  # add it to our result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers `numbers` as input and returns a new list with duplicates removed. It uses a dictionary `seen` to keep track of the numbers it has seen before, and a list `result` to store the final result. The function iterates over the input list, and for each number, it checks if it has been seen before. If not, it marks it as seen and adds it to the result list.