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
    # Create an OrderedDict to store the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            count_dict[num] = 1

    # Create a new list with numbers that occur only once
    unique_numbers = [num for num, count in count_dict.items() if count == 1]

    return unique_numbers

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses an OrderedDict to keep track of the count of each number in the input list. It then creates a new list with numbers that occur only once. The order of elements in the output list is the same as in the input list.

Alternatively, you can use a different approach with a list comprehension and the `count()` method:

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
    return [num for i, num in enumerate(numbers) if numbers.count(num) == 1]

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this approach is less efficient than the first one, especially for large input lists, because the `count()` method has to scan the entire list for each number.