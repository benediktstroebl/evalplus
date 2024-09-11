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
    # Use OrderedDict to keep track of the count of each element while preserving order
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Return a list of keys (numbers) that have a count of 1
    return [num for num, count in count_dict.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise version using a dictionary comprehension:

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
    # Use OrderedDict to keep track of the count of each element while preserving order
    count_dict = OrderedDict((num, numbers.count(num)) for num in numbers)

    # Return a list of keys (numbers) that have a count of 1
    return [num for num, count in count_dict.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, be aware that the `numbers.count(num)` call in the dictionary comprehension has a time complexity of O(n), making this version less efficient than the first one for large lists.