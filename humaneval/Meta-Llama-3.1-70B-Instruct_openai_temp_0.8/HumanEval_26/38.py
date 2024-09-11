```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with no duplicates.
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

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers and returns a new list where all elements that occur more than once in the original list are removed. The function uses two sets, `seen` and `seen_twice`, to keep track of the elements it has seen so far. The `seen` set contains elements that have been seen once, and the `seen_twice` set contains elements that have been seen more than once.

The function iterates over the input list, and for each element, it checks if it is in the `seen_twice` set. If it is, the function skips it. If it is in the `seen` set, the function adds it to the `seen_twice` set and removes it from the result list. If it is not in either set, the function adds it to the `seen` set and the result list.

Finally, the function returns the result list.