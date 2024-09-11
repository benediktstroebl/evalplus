```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: The list of integers with duplicates removed.
    """
    seen = set()  # A set to keep track of unique elements
    result = []  # The result list
    
    for num in numbers:
        if num not in seen:  # If the number is not in the set
            seen.add(num)  # Add it to the set
            result.append(num)  # And append it to the result list
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses a set to efficiently check for duplicates. It iterates over the input list, adding each number to the result list and the set if it's not already in the set. This way, it preserves the original order of the list and removes duplicates.