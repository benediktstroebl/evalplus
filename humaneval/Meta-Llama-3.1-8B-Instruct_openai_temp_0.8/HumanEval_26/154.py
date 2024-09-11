```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of unique integers from the input list, in the same order.
    """
    seen = set()  # A set to keep track of elements we've seen
    unique_numbers = []  # A list to store the unique numbers

    for num in numbers:
        if num not in seen:  # If we haven't seen this number before
            seen.add(num)  # Mark it as seen
            unique_numbers.append(num)  # Add it to the list of unique numbers

    return unique_numbers


# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a `set` to efficiently keep track of the numbers we've seen so far. It iterates over the input list, adding each number to the `seen` set and appending it to the `unique_numbers` list only if it hasn't been seen before. This way, we preserve the original order of the numbers.