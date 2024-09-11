```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed.
    """
    # Create an OrderedDict to keep track of the count of each number
    # and to preserve the order of elements
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter out the numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can use Python's built-in `dict` (which preserves insertion order in Python 3.7+) to simplify the code:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed.
    """
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    return [num for num, count in count_dict.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this version may not work as expected in Python versions before 3.7, since dictionaries did not preserve insertion order in those versions.