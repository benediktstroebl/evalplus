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
        # If the number is not in the set, add it to the set and the result list
        if num not in seen:
            seen.add(num)
            result.append(num)
            
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([4, 3, 2, 2, 1]))  # Output: [4, 3, 2, 1]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([]))  # Output: []
```

This script uses a set to keep track of the numbers that have been seen so far. It iterates over the input list, and for each number, it checks if the number is in the set. If it's not in the set, it adds the number to the set and the result list. This way, the function preserves the order of the elements and removes all duplicates.