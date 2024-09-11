### Remove Duplicates from a List
#### Problem Description:
From a list of integers, remove all elements that occur more than once. Keep order of elements left the same as in the input.

#### Solution:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): The input list of integers.

    Returns:
    List[int]: The list of integers with elements that occur more than once removed.
    """
    seen = set()  # A set to keep track of elements we've seen
    result = []    # The result list

    for num in numbers:
        if num not in seen:  # If the number is not seen before
            seen.add(num)    # Add it to the set of seen numbers
            result.append(num)  # Add it to the result list

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

### Explanation:
This script uses a set to keep track of the elements it has seen. If an element is not in the set, it is added to both the set and the result list. This way, we ensure that each element is added to the result list at most once. The script then returns the result list.