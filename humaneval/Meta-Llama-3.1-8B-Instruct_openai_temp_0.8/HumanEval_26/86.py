### Remove Duplicates from a List of Integers
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of unique integers in the original order.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    unique_numbers = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    
    return unique_numbers

# Example usage:
numbers = [1, 2, 3, 2, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that removes all elements from a list of integers that occur more than once. It keeps the order of elements in the list the same as in the input. The function uses a `set` to keep track of unique elements seen so far. It iterates over the input list and appends each element to the result list only if it has not been seen before. The example usage at the end demonstrates how to use this function.