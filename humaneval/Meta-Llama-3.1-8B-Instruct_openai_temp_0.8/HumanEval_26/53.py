```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with all elements that occur more than once removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Create a dictionary to store the count of each number
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Create a new list that includes only the numbers that occur once
    result = []
    for num in numbers:
        if count_dict[num] == 1:
            result.append(num)

    return result


# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that includes only the integers that occur more than once. The function uses a dictionary to count the occurrences of each integer in the input list, and then creates a new list that includes only the integers with a count of 1. The script includes a test case to demonstrate the function's behavior.