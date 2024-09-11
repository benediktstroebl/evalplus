```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A list of integers with duplicates removed.
    """
    
    # Create an ordered dictionary to store the count of each number
    count_dict = OrderedDict()
    
    # Iterate over the input list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Use a list comprehension to create a new list with numbers that occur only once
    return [num for num, count in count_dict.items() if count == 1]


# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input, removes the duplicates (i.e., the numbers that occur more than once), and returns the resulting list. The function uses an ordered dictionary to count the occurrence of each number and then uses a list comprehension to create a new list with the numbers that occur only once. The example usage demonstrates how to call the function with the input `[1, 2, 3, 2, 4]` and prints the output `[1, 3, 4]`.