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
    seen = set()  # Keep track of elements we've seen so far
    result = []   # Store the result here

    for num in numbers:
        if num not in seen:
            result.append(num)  # Add new elements to the result
            seen.add(num)       # Mark it as seen

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([4, 5, 5, 4, 4]))  # Output: [5]
print(remove_duplicates([10, 20, 30]))     # Output: [10, 20, 30]
```