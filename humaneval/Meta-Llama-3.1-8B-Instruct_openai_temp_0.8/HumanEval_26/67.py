### remove_duplicates Function
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of unique integers in the original order

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # Keep track of seen elements
    result = []   # Result list

    for num in numbers:
        if num not in seen:  # If the number is not seen yet
            seen.add(num)    # Mark it as seen
            result.append(num)  # Add it to the result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
In this script, we create a set `seen` to keep track of the elements we've seen so far. We iterate over the input list `numbers`, and for each number, we check if it's in the `seen` set. If it's not, we add it to the `seen` set and the result list. This way, we ensure we only keep the unique elements in the original order.