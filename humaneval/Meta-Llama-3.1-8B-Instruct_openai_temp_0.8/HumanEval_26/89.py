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
    seen = set()  # Initialize an empty set to keep track of seen elements
    result = []   # Initialize an empty list to store the result

    for num in numbers:
        # If the current number is not in the seen set, add it to the result list and the seen set
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This script uses a set to keep track of elements that have been seen so far. It iterates over the input list, and for each element, it checks if it's in the seen set. If not, it adds the element to the result list and the seen set. This approach ensures that the order of elements in the result list is the same as in the input list.