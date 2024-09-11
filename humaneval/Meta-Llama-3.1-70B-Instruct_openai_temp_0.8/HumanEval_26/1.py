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
    # Create an ordered dictionary to store the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # Otherwise, add the number to the dictionary with a count of 1
        else:
            count_dict[num] = 1

    # Create a new list with only the numbers that have a count of 1
    unique_numbers = [num for num, count in count_dict.items() if count == 1]

    return unique_numbers

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

Alternatively, you can use a more Pythonic way to solve this problem using a list comprehension and the `collections.Counter` class:

```python
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers with duplicates removed.
    """
    count = Counter(numbers)
    return [num for num in numbers if count[num] == 1]

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```