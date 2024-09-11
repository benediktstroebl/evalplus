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
    counts = OrderedDict((num, numbers.count(num)) for num in numbers)
    
    # Filter out numbers that occur more than once
    result = [num for num, count in counts.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([5, 5, 5, 2, 2]))  # []
print(remove_duplicates([10, 20, 30, 40, 50]))  # [10, 20, 30, 40, 50]
```