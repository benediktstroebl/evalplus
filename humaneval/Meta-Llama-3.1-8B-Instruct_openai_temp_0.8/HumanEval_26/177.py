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
    # Create an empty dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate over the list of numbers
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # Otherwise, add the number to the dictionary with a count of 1
        else:
            freq_dict[num] = 1
    
    # Create an empty list to store the numbers that occur only once
    unique_nums = []
    
    # Iterate over the original list of numbers again
    for num in numbers:
        # If a number occurs only once, add it to the list of unique numbers
        if freq_dict[num] == 1:
            unique_nums.append(num)
    
    # Return the list of unique numbers
    return unique_nums

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicates removed. The function works by creating a dictionary to store the frequency of each number in the list, and then iterating over the list again to add numbers that occur only once to a new list. The new list is then returned as the result. The script includes a test case to demonstrate the function's behavior.