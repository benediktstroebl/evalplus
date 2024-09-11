```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with elements occurring more than once removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty dictionary to store the frequency of each number
    num_freq = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary or its frequency is 0
        if num not in num_freq or num_freq[num] == 0:
            # Increment the frequency of the number
            num_freq[num] = num_freq.get(num, 0) + 1
            # Append the number to the result list
            result.append(num)
    
    # Return the result list
    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))
```

This script defines the `remove_duplicates` function, which iterates over the input list and appends each number to the result list only if it's not already in the result list or if its frequency is 0 in the `num_freq` dictionary. It then returns the result list. The script also includes a test case to demonstrate the function's behavior.