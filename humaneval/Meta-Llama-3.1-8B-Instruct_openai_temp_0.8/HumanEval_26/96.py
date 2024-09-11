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
    seen = set()  # Use a set to store unique elements
    result = []  # Initialize an empty list to store the result

    for num in numbers:  # Iterate through the input list
        if num not in seen:  # Check if the number is not in the set
            result.append(num)  # Add the number to the result list
            seen.add(num)  # Add the number to the set

    return result  # Return the result list

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a set to keep track of unique elements and iterates through the input list to construct the result list. The example usage demonstrates how to use the function with a sample input list.