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

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # A set to keep track of seen elements
    result = []  # The final list without duplicates

    for num in numbers:
        if num not in seen:  # If the current element has not been seen
            result.append(num)  # Add it to the result list
            seen.add(num)  # Mark it as seen

    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
```

This script uses a set (`seen`) to keep track of elements that have been seen so far. It iterates over the input list, adding elements to the result list only if they have not been seen before. This approach ensures that the order of elements is preserved and elements with a count greater than 1 are removed.