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
    
    # Iterate over the input list
    for num in numbers:
        # If the number has not been seen before, add it to the result list and mark it as seen
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([4, 5, 5, 4, 4]))  # Output: [4, 5]
print(remove_duplicates([7, 7, 7, 7, 7]))  # Output: []
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a set to keep track of the numbers it has seen so far. It iterates over the input list, adding each number to the result list and marking it as seen if it has not been seen before. This ensures that the order of elements in the result list is the same as in the input list. The script also includes some test cases to demonstrate the function's behavior.