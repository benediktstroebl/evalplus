```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    :param numbers: A list of integers
    :return: A list of integers with no duplicates
    """
    # Create an OrderedDict to automatically remove duplicates
    # while preserving the order of the elements
    ordered_set = OrderedDict((num, True) for num in numbers)
    
    # Return a list of keys from the OrderedDict
    return list(ordered_set.keys())


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
print(remove_duplicates([5, 5, 5, 1, 2, 3]))  # Output: [5, 1, 2, 3]
print(remove_duplicates([]))  # Output: []
```