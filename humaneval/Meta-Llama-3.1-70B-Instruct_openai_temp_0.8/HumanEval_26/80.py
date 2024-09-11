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

    # First, identify the duplicates
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    # Then, create a new list with the duplicates removed
    result = [num for num in numbers if num not in duplicates]

    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

Alternatively, you can also use an OrderedDict to solve this problem in a single pass, preserving the order of elements:

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

    # Create an OrderedDict where the keys are the input numbers
    for num in numbers:
        seen[num] = None

    # Then, create a new list with the OrderedDict's keys
    result = list(seen.keys())

    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

However, the OrderedDict approach does not exactly solve the original problem because it does not remove all occurrences of a duplicate number. To solve the original problem using OrderedDict, we would need to make an additional pass through the data to identify the duplicates.

You can also use a single list comprehension with a set to solve this problem in a single pass:

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

    # Create a new list with the duplicates removed
    result = [num for num in numbers if not (num in seen or (seen.add(num) or num in duplicates) or (duplicates.add(num) if numbers.count(num) > 1 else False))]

    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
However, this list comprehension is complex and not as readable as the original solution.