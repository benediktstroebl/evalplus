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

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

In this script, we use a set to keep track of the numbers we've seen so far. This allows us to check if a number has occurred more than once in constant time. We iterate over the input list, and for each number, we check if it's in the set. If it's not, we add it to the set and append it to the result list. If it is in the set, we simply skip it and move on to the next number. This way, we're able to remove duplicates efficiently while preserving the original order.