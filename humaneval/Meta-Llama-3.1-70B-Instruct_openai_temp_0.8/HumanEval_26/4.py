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
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

This script uses two sets, `seen` and `seen_twice`, to keep track of the numbers it has seen so far. The `seen` set stores the numbers that have been seen only once, and the `seen_twice` set stores the numbers that have been seen more than once.

The script iterates over the input list. If a number has been seen more than once (i.e., it's in `seen_twice`), it's skipped. If a number has been seen only once (i.e., it's in `seen`), it's marked as seen twice and removed from the result list. If a number hasn't been seen before, it's added to `seen` and the result list.

Finally, the script returns the result list, which contains the unique numbers from the input list, in the original order.