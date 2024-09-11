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
    # Create an ordered dictionary to keep track of element counts
    counts = OrderedDict()
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in counts:
            counts[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            counts[num] = 1

    # Filter out numbers that occur more than once
    unique_numbers = [num for num, count in counts.items() if count == 1]

    return unique_numbers


# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise version with a dictionary and list comprehension:

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

    # Find duplicates and keep track of seen elements
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    # Filter out numbers that occur more than once
    unique_numbers = [num for num in numbers if num not in duplicates]

    return unique_numbers


# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```