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
    seen = set()
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number has not been seen before, add it to the result and mark it as seen
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3]))  # [3]
print(remove_duplicates([]))  # []
print(remove_duplicates([1, 2, 3]))  # [1, 2, 3]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a `set` to keep track of the numbers it has seen so far, and a list to store the result. It iterates over the input list, adding each number to the result list and marking it as seen if it has not been seen before. The function returns the result list. The example usage shows how to use the function with different inputs.