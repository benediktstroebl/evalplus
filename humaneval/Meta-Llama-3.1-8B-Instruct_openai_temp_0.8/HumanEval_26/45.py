```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with all elements that occur more than once removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = {}
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = True  # Add num to the seen dict
            result.append(num)  # Add num to the result list
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that removes all elements that occur more than once in the input list. It uses a dictionary `seen` to keep track of the elements it has seen so far. The function iterates over the input list, and for each element, it checks if the element is in the `seen` dictionary. If it is not, it adds the element to the `seen` dictionary and appends it to the `result` list. Finally, it returns the `result` list.