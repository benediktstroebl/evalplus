```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The input list with duplicates removed.
    """
    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

In this script, we use a set to keep track of numbers we have seen so far. We iterate over the list of numbers, and for each number, we check if it's in the set of seen numbers. If it's not, we add it to the set and append it to the result list. This way, we avoid adding duplicate numbers to the result list while preserving the original order of elements.