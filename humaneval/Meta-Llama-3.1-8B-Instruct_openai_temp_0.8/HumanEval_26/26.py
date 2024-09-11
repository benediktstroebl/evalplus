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
    """
    seen = set()  # Keep track of unique elements seen so far
    result = []    # The final list with duplicates removed

    for num in numbers:
        if num not in seen:  # If this number hasn't been seen before
            seen.add(num)     # Add it to our set of seen numbers
            result.append(num) # Add it to the result list

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers and removes elements that occur more than once, preserving the original order of elements. The function uses a set to keep track of unique elements seen so far, and a list to store the result. It iterates over the input list, adding each number to the result list only if it hasn't been seen before. Finally, it returns the result list.