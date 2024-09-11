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
    
    # Iterate through the input list
    for num in numbers:
        # If the number is not in the set, add it to the set and the result list
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This script uses a set to keep track of the numbers it has seen. It iterates through the input list and adds each number to the result list only if it hasn't been seen before. The result list is then returned as the output.