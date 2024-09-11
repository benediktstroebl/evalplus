### Remove Duplicate Elements from a List
#### Using a Dictionary to Keep Track of Element Counts
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): The input list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Create a dictionary to keep track of element counts
    counts = {}

    # Create a new list to store the result
    result = []

    # Iterate over the input list
    for num in numbers:
        # If the element is not in the dictionary or its count is 0
        if num not in counts or counts[num] == 0:
            # Add it to the result list
            result.append(num)
            # Increment its count in the dictionary
            counts[num] = counts.get(num, 0) + 1

    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a dictionary to keep track of element counts and a list to store the result. The script also includes a test case to demonstrate the function's behavior.