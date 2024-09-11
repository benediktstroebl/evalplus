```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with no duplicates.
    """
    # Create an ordered dictionary to keep track of the count of each number
    count_dict = OrderedDict()
    
    # Iterate over the input list
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            count_dict[num] = 1
    
    # Create a new list with only the numbers that occur once
    unique_numbers = [num for num, count in count_dict.items() if count == 1]
    
    return unique_numbers


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicate elements removed, preserving the original order. It uses an `OrderedDict` to count the occurrences of each number, then creates a new list with only the numbers that occur once. The test case at the end verifies the function's correctness.