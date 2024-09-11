```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): The list of integers from which to remove duplicates.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    seen = set()  # Keep track of elements we've seen so far
    result = []  # The list of elements with no duplicates

    for num in numbers:
        if num not in seen:
            # If the number is not in the seen set, add it to the result list and the seen set
            result.append(num)
            seen.add(num)

    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This Python script defines a function `remove_duplicates` that removes all elements from a list that occur more than once, while preserving their original order. It uses a set to keep track of elements it has seen so far, and appends each new element to both the result list and the seen set only if it has not been seen before. The example usage at the end demonstrates how to call this function with a sample list of numbers.