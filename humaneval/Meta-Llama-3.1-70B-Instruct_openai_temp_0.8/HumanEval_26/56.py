```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    seen = OrderedDict()
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    return [num for num, count in seen.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
This script uses an OrderedDict to keep track of the count of each number in the input list. It then uses a list comprehension to return a new list containing only the numbers that occur once. The order of the elements in the output list is the same as their first occurrence in the input list.

Alternatively, you can use a more concise solution using dict and a list comprehension:

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
    seen = {}
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    return [num for num in numbers if seen[num] == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, please note that in Python 3.7 and later, the built-in dict maintains the insertion order, so you can use a regular dict instead of OrderedDict in this case.