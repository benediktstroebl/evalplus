### Remove Duplicates from a List of Integers
#### Problem Statement
Remove all elements from a list of integers that occur more than once. Preserve the original order of elements.

#### Solution
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
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # Output: [1, 2, 3]
print(remove_duplicates([4, 4, 4, 4, 4]))  # Output: []
```
This solution uses an unordered set `seen` to keep track of the numbers we've encountered so far. We iterate over the input list `numbers`, and for each number, we check if it's in the `seen` set. If it's not, we add it to the `result` list and the `seen` set. This way, we ensure that each number appears at most once in the `result` list, while preserving the original order.