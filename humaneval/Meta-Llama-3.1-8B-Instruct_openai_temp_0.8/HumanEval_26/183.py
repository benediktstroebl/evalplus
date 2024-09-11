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

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # Initialize an empty set to keep track of seen numbers
    result = []  # Initialize an empty list to store the result

    for num in numbers:
        # If the number has not been seen before, add it to the result and mark it as seen
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result  # Return the result list

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

Alternatively, you can use a dictionary to keep track of the count of each number and then iterate through the list again to add numbers that have a count of 1 to the result list. Here is how you can do it:

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

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    counts = {}  # Initialize an empty dictionary to store the count of each number
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1  # Increment the count of the number

    result = []  # Initialize an empty list to store the result
    for num in numbers:
        # If the number has a count of 1, add it to the result
        if counts[num] == 1:
            result.append(num)

    return result  # Return the result list

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```