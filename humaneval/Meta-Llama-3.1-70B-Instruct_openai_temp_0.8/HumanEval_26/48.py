```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): The input list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.
    """
    # Create an OrderedDict to keep track of the count of each element
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter out elements that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

This script first counts the occurrence of each number in the list using an OrderedDict, which preserves the order of elements. It then filters out the numbers that occur more than once and returns the result. The test case at the end demonstrates the usage of the function.