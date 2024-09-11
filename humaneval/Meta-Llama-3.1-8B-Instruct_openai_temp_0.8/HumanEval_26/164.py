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
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))
```

This script uses a set to keep track of elements we have seen so far. We iterate through the input list, and for each number, we check if it's already in the set. If not, we add it to the result list and the set. This way, we ensure that we don't include any duplicates in the result. The time complexity is O(n), where n is the number of elements in the input list.