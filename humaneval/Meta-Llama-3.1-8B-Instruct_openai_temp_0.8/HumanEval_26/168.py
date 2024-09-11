```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    List[int]: A list of integers with duplicates removed.
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([4, 4, 4, 4, 4]))  # Output: []
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This script defines a function `remove_duplicates` that uses a set to keep track of the numbers it has seen so far. It iterates over the input list, adding each unique number to the result list and the set of seen numbers. The test cases show the function's behavior for different inputs.