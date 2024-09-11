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
    List[int]: A list of integers with no duplicates.
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

    # Create a new list with only the numbers that occur once
    result = [num for num, count in count_dict.items() if count == 1]

    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script works by first creating an `OrderedDict` to store the count of each number in the input list. The `OrderedDict` is used to preserve the order of the elements. Then, it creates a new list with only the numbers that occur once.