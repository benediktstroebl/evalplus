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
    # Use an OrderedDict to keep track of counts and maintain order
    counts = OrderedDict()
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Return a list of numbers with a count of 1
    return [num for num, count in counts.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

Alternatively, you can use a combination of list comprehension and the `count` method of lists:

```python
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
    return [num for num in numbers if num not in seen and not (seen.add(num) or numbers.count(num) > 1)]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

However, this approach has a time complexity of O(n^2) due to the `count` method. The first approach using `OrderedDict` has a time complexity of O(n).