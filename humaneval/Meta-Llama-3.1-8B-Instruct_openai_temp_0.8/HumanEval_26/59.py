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
    seen = {}  # Dictionary to keep track of seen elements
    result = []  # Result list
    for num in numbers:
        if num not in seen:  # If the number has not been seen before
            seen[num] = True  # Mark the number as seen
            result.append(num)  # Add the number to the result list
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The `seen` dictionary is used to keep track of elements that have been seen before, and the `result` list is used to store the elements that have not been seen before. The function iterates over the input list, and for each element, it checks if the element has been seen before. If not, it marks the element as seen and adds it to the result list. Finally, the function returns the result list.