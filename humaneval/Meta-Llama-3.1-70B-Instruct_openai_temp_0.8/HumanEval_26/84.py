```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers

    Returns:
        A list of integers with duplicates removed
    """
    # Create an OrderedDict to keep track of the count of each number
    count_dict = OrderedDict()
    
    # Iterate over the input list
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            count_dict[num] = 1
    
    # Use a list comprehension to create the output list
    # Include only numbers that have a count of 1
    return [num for num, count in count_dict.items() if count == 1]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```