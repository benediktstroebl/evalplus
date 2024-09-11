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
    # Create an OrderedDict to count the occurrence of each number
    # and maintain their insertion order
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Filter out numbers that occur more than once
    result = [num for num, count in counts.items() if count == 1]
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```