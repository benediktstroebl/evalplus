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
    # Create an OrderedDict to keep track of the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script works by first creating an `OrderedDict` that maps each number to its count in the input list. It then uses a list comprehension to filter out the numbers that occur more than once. The `OrderedDict` is used to preserve the original order of the numbers.