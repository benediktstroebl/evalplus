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
    # Count occurrences of each number while preserving order
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Return numbers that occur only once
    return [num for num, count in counts.items() if count == 1]


# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicates removed. The function preserves the original order of elements. The `OrderedDict` is used to count occurrences of each number while preserving the order of first occurrence. The function then uses a list comprehension to return numbers that occur only once. The example usage demonstrates how to use the function with a sample list `[1, 2, 3, 2, 4]`.