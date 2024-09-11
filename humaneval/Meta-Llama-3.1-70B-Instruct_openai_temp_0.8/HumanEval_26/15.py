```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Count occurrences of each number
    count = OrderedDict()
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Filter out numbers that occur more than once
    result = [num for num, freq in count.items() if freq == 1]

    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list where all elements that occur more than once are removed. The function uses an `OrderedDict` to count the occurrences of each number, preserving the original order. Then, it uses a list comprehension to filter out numbers that occur more than once.

However, if you're using Python 3.7 or later, you can use a regular dictionary (`dict`) instead of `OrderedDict`, as dictionaries remember the order of items inserted.

Alternatively, if you prefer a more concise solution, you can use this version:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            if numbers.count(num) == 1:
                result.append(num)
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, the `count` method has a time complexity of O(n), making the overall time complexity of this version O(n^2). Therefore, the first version is generally more efficient, especially for large lists.