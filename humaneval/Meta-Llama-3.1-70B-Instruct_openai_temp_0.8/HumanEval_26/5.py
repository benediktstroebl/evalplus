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
    List[int]: The list of integers with duplicates removed.
    """
    # Create an OrderedDict to keep track of the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Create a new list with numbers that occur only once
    unique_numbers = [num for num, count in count_dict.items() if count == 1]

    return unique_numbers

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

Alternatively, you can use Python's built-in `list.count()` method in a list comprehension:

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: The list of integers with duplicates removed.
    """
    return [num for i, num in enumerate(numbers) if numbers.count(num) == 1 and numbers.index(num) == i]

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```