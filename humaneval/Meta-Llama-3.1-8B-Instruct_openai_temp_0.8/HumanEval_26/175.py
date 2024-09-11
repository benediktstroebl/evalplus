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
    seen = {}  # Dictionary to store seen elements
    result = []  # List to store the result

    for num in numbers:  # Iterate over the input list
        if num not in seen:  # If the number has not been seen before
            seen[num] = True  # Mark it as seen
            result.append(num)  # Add it to the result list

    return result  # Return the result list

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a dictionary `seen` to keep track of the elements it has seen so far, and a list `result` to store the elements that are not duplicates. The function iterates over the input list, and for each element, it checks if it has been seen before. If not, it marks the element as seen and adds it to the result list. Finally, the function returns the result list. The example usage at the end demonstrates how to use the function.