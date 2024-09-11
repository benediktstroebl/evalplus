```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of integers with duplicates removed
    """
    # Create an OrderedDict to store the first occurrence of each number
    ordered_dict = OrderedDict()
    for num in numbers:
        if num not in ordered_dict:
            ordered_dict[num] = 1
        else:
            ordered_dict[num] += 1

    # Filter out the numbers that occur more than once
    result = [num for num, count in ordered_dict.items() if count == 1]

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

This script uses an `OrderedDict` to store the first occurrence of each number in the input list, along with its count. Then it filters out the numbers that occur more than once, preserving the original order of the remaining numbers.