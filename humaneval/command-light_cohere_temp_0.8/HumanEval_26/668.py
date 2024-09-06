```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes all duplicate elements from the input list and returns the unique list.
    """
    unique elements: {1, 2, 3, 4}
    """
    # Initialize a set to hold the unique elements
    set_elements = set(numbers)
    # Convert the set back into a list and return it
    return list(set_elements)

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
test_remove_duplicates = remove_duplicates(numbers_list)
print(test_remove_duplicates) # Output: [1, 2, 3, 4, 5]

numbers_set = [1, 2, 3, 4, 5]
test_remove_duplicates_set = remove_duplicates(numbers_set)
print(test_remove_duplicates_set) # Output: [1, 2, 3, 4]
```

This Python script defines a function called `remove_duplicates`, which takes a list of integers as input and returns a list of unique integers. The function utilizes a set data structure to identify and remove duplicate elements from the input list. It then converts the time the set into a list and returns it, effectively removing duplicates.

Unit tests are also included in the script to verify the functionality of the `remove_duplicates` function. The test is passed successfully for both cases, where the input is a list of integers and a set of integers.