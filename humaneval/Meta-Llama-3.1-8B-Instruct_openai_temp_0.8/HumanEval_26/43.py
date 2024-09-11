### Remove Duplicate Elements from a List
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
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a set `seen` to keep track of the elements it has seen so far, and appends each element to the result list if it hasn't been seen before. The example usage at the end shows how to use this function with the input `[1, 2, 3, 2, 4]`, which is expected to output `[1, 3, 4]`.