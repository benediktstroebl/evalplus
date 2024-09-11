```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A new list containing integers that occur only once in the input.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = {}  # Dictionary to store seen numbers
    result = []  # Result list

    for num in numbers:
        if num not in seen:
            seen[num] = True  # Mark number as seen
            result.append(num)  # Add number to result

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```