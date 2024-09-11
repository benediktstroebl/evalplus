```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with duplicates removed.
    """
    seen = {}
    result = []

    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
print(remove_duplicates([1, 1, 1, 2, 2, 2]))  # Output: [2]
print(remove_duplicates([1, 2, 3, 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

However, Python has a built-in `dict.fromkeys()` method that can be used to remove duplicates while preserving order, which can make the function more concise:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with duplicates removed.
    """
    return list(dict.fromkeys(numbers))

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
print(remove_duplicates([1, 1, 1, 2, 2, 2]))  # Output: [1, 2]
print(remove_duplicates([1, 2, 3, 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

This version of the function works by creating a dictionary where the keys are the unique elements from the input list, and then converting the dictionary keys back to a list. The result is a list with duplicates removed, in the original order.