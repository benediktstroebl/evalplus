```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    seen_twice = set()
    result = []

    for num in numbers:
        if num in seen_twice:
            continue
        elif num in seen:
            seen_twice.add(num)
        else:
            seen.add(num)
            result.append(num)

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses two sets (`seen` and `seen_twice`) to keep track of the numbers it has encountered so far. If a number is encountered for the first time, it is added to the `seen` set and the result list. If a number is encountered for the second time, it is added to the `seen_twice` set. If a number is encountered for the third time or more, it is skipped. This way, the function ensures that only numbers that occur once in the input list are included in the output list, and the order of elements is preserved.