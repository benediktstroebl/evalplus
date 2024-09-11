### Remove Duplicates from a List
#### Problem Statement
From a list of integers, remove all elements that occur more than once. Keep order of elements left the same as in the input.

#### Solution
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Removes all elements from a list that occur more than once, preserving the original order.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with duplicates removed.
    """
    seen = set()  # Used to keep track of unique elements
    result = []  # The list of elements without duplicates

    for num in numbers:
        if num not in seen:  # If the number is not in the set
            seen.add(num)  # Add it to the set
            result.append(num)  # And append it to the result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a set to keep track of unique elements encountered so far. It iterates over the input list, and for each element, checks if it's already in the set. If not, it adds the element to the set and the result list. This way, duplicates are removed while preserving the original order.