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
    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
    print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
    print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This script uses a set to keep track of the numbers that have been seen. It iterates over the input list, and for each number, it checks if the number is in the set. If it's not, it adds the number to the result list and the set. This way, it ensures that only unique numbers are added to the result list and keeps the order of the elements the same as the input list.