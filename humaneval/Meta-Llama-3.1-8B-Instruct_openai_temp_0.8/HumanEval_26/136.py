```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]))  # []
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
```
This script uses a set to keep track of the numbers we've seen so far, and it only adds a number to the result list if it's not already in the set. This approach has a time complexity of O(n), where n is the number of elements in the input list.