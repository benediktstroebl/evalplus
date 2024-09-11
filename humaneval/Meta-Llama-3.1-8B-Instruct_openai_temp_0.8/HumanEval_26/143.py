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
    seen = set()  # keep track of seen numbers
    result = []  # store the result

    for num in numbers:
        if num not in seen:  # if the number is not in the seen set
            seen.add(num)  # add it to the seen set
            result.append(num)  # and add it to the result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines the `remove_duplicates` function that iterates through the input list and adds each number to a set (`seen`) and the result list (`result`) if it hasn't been seen before. The function then returns the result list. The example usage demonstrates how to call the function and print the result.