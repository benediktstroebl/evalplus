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
        seen[num] = None  # The value doesn't matter here

    # Filter out numbers that have more than one occurrence in the original list
    return [num for num in seen if numbers.count(num) == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
However, the above solution isn't very efficient, especially for large lists, because it uses `numbers.count(num)` for each unique number.

Here's an improved version that only iterates over the list twice:

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
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    return [num for num in numbers if num not in duplicates]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
This solution works by first identifying all the duplicate numbers, then filtering them out of the original list.