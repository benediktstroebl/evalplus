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
    List[int]: A list of integers with all duplicates removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = OrderedDict()  # Initialize an ordered dictionary
    for num in numbers:  # Iterate through the list
        seen[num] = None  # Add each element to the dictionary
    # Create a list of keys from the dictionary (automatically removes duplicates)
    # and only keep keys that appear once in the original list
    result = [num for num in seen if numbers.count(num) == 1]
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

Alternatively, a more concise and efficient solution using Python's built-in Counter class from the collections module:

```python
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with all duplicates removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count = Counter(numbers)  # Count the occurrences of each number
    # Keep numbers that appear once
    return [num for num in numbers if count[num] == 1]

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

This version avoids the overhead of creating a list of keys and then filtering them, and is thus likely to be more efficient for large lists.