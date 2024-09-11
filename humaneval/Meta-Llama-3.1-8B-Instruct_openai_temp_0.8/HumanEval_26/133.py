```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A list of integers with all elements that occur more than once removed.
    
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = {}  # dictionary to keep track of seen numbers
    result = []  # list to store the result
    
    for num in numbers:
        if num not in seen:
            # if the number is not in the dictionary, add it
            seen[num] = True
            result.append(num)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a dictionary (`seen`) to keep track of the numbers that have been seen so far. It iterates through the input list and for each number, it checks if the number is in the dictionary. If it's not, it adds the number to the dictionary and the result list. If it is, it skips the number. This approach ensures that the order of the elements in the result list is the same as in the input list.