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
    
    # Count the occurrences of each element
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Filter out elements with more than one occurrence
    unique_numbers = [num for num, count in counts.items() if count == 1]
    
    return unique_numbers


# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This script uses an OrderedDict to keep track of the counts of each element in the input list, then uses a list comprehension to filter out elements that occur more than once. The resulting list is returned by the `remove_duplicates` function.