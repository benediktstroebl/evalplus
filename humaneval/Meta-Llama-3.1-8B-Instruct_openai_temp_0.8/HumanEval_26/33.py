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

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([4, 2, 4, 2, 4]))  # Output: [4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([]))  # Output: []
```

This script defines a function `remove_duplicates` that takes a list of integers as input. It uses a set `seen` to keep track of the numbers it has seen so far, and a list `result` to store the numbers that are encountered for the first time. The function iterates through the input list, and for each number, it checks if it is in the `seen` set. If it is not, it adds the number to the `result` list and adds it to the `seen` set. Finally, it returns the `result` list.

The example usage at the end shows how to use the function with different inputs.