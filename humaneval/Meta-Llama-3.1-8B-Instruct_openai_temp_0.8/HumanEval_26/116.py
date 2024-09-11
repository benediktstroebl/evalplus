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
    unique_numbers = []

    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)

    return unique_numbers

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a set to keep track of the elements it has seen so far. When an element is encountered for the first time, it is added to the `unique_numbers` list and to the `seen` set. This way, when the same element is seen again, it is already in the `seen` set, so it is skipped. This approach ensures that the order of the elements is preserved.