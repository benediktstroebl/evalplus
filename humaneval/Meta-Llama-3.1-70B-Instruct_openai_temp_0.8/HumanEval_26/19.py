```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of integers with duplicates removed
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
```

In this script, we iterate over the input list. We use two sets to keep track of the numbers that we have seen so far: `seen` for numbers that we have seen once, and `seen_twice` for numbers that we have seen more than once. If we encounter a number that is in `seen_twice`, we skip it. If we encounter a number that is in `seen`, we add it to `seen_twice` and remove it from the result. If we encounter a number that is not in `seen`, we add it to `seen` and append it to the result. This way, we ensure that the numbers in the result list appear in the same order as in the input list.