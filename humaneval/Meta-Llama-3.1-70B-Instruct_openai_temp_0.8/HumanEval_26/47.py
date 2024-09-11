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
    # Create an OrderedDict to store the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]

    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script works by first creating an `OrderedDict` where the keys are the numbers in the input list and the values are their respective counts. Then, it uses a list comprehension to create a new list that only includes numbers with a count of 1. This approach preserves the original order of elements in the input list.

Alternatively, you can use a different approach with Python's built-in `list.count()` function:

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
    result = []
    for num in numbers:
        if numbers.count(num) == 1:
            result.append(num)
    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this approach has a time complexity of O(n^2) due to the `list.count()` function, whereas the first approach has a time complexity of O(n). Therefore, the first approach is generally more efficient for large input lists.