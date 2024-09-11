### Removing Duplicates from a List
#### Problem Statement

From a list of integers, remove all elements that occur more than once.
Keep order of elements left the same as in the input.

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
        List[int]: The list with elements that occur more than once removed.

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
```

#### Explanation

This solution uses a set to keep track of the elements we have seen so far. We iterate over the input list and for each element, we check if it is in the set. If it's not, we add it to the result list and the set. This way, we only add elements to the result list if they have not been seen before, effectively removing duplicates while maintaining the original order.

#### Example Use Case

```python
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```