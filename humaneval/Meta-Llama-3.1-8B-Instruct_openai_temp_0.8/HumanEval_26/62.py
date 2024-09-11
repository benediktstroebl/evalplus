### Python Script to Remove Duplicates from a List
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): The list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This script uses a set to keep track of the numbers that have been seen so far. It iterates over the list of numbers, adding each number to the result list if it hasn't been seen before. The `seen` set is used to check if a number has been seen, and it's updated with the new number whenever a duplicate is found. The result is a list of numbers with duplicates removed, in the original order.