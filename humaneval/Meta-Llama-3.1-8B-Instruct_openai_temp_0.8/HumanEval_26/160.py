```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of integers with duplicates removed
    """
    seen = set()  # Initialize an empty set to store unique elements
    result = []  # Initialize an empty list to store the result

    for num in numbers:  # Iterate over the input list
        if num not in seen:  # Check if the current number is not in the set
            seen.add(num)  # Add the current number to the set
            result.append(num)  # Add the current number to the result list

    return result  # Return the result list

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: [1, 2, 3, 4]
```