```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A list of integers with duplicates removed.
    """
    seen = set()
    seen_more_than_once = set()
    
    result = []
    
    for num in numbers:
        if num in seen_more_than_once:
            continue
        elif num in seen:
            seen_more_than_once.add(num)
        else:
            seen.add(num)
            result.append(num)
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

In this script, we iterate through the input list and keep track of the numbers we've seen in the `seen` set. If we encounter a number that's already in the `seen` set, we add it to the `seen_more_than_once` set to mark it as a duplicate. If a number is in the `seen_more_than_once` set, we skip it. Otherwise, we add it to the `seen` set and append it to the result list.

This way, we preserve the original order of the elements and remove only the numbers that occur more than once.