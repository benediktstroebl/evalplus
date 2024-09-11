```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: The input list with duplicates removed.
    """
    seen = set()
    seen_twice = set()
    result = []

    for num in numbers:
        if num in seen_twice:
            continue
        elif num in seen:
            seen_twice.add(num)
            result.remove(num)
        else:
            seen.add(num)
            result.append(num)

    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 1, 2, 2, 3]))  # Output: [3]
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This Python script defines a function `remove_duplicates` that takes a list of integers and returns the list with all duplicates removed. The function maintains the original order of the elements. It uses two sets, `seen` and `seen_twice`, to track the numbers it has encountered so far and the numbers that have appeared more than once, respectively. The result list is constructed and updated based on these sets.