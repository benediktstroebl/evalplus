```markdown
### Remove Duplicates from a List of Integers

This script defines a function `remove_duplicates` that removes all elements from a list of integers that occur more than once, preserving the original order of elements.
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: The list of integers with duplicates removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a dictionary to store the count of each number
    count_dict = {}
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            count_dict[num] = 1

    # Create a new list that includes only the numbers with a count of 1
    result = [num for num, count in count_dict.items() if count == 1]

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

### Explanation

This script uses a dictionary to keep track of the count of each number in the input list. It then creates a new list that includes only the numbers with a count of 1, effectively removing all duplicates while preserving the original order.