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
    # Count the occurrence of each number
    count = OrderedDict()
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Filter out numbers that occur more than once
    result = [num for num, freq in count.items() if freq == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```