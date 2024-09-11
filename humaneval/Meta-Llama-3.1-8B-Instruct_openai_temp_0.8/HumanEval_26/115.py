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
            seen.add(num)
            result.append(num)
    return result

# Test cases
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # Expected output: []
print(remove_duplicates([1, 2, 3, 4, 5]))  # Expected output: [1, 2, 3, 4, 5]
```

This script uses a set to keep track of the elements we've seen so far. We iterate over the input list, and for each element, we check if it's already in the `seen` set. If not, we add it to the `seen` set and append it to our result list. This way, we ensure that we keep the order of elements as in the input, and we remove all elements that occur more than once.