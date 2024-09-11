```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Initialize an empty OrderedDict to store unique elements and their counts
    element_counts = OrderedDict()
    
    # Iterate over the input list
    for num in numbers:
        # If the element is already in the OrderedDict, increment its count
        if num in element_counts:
            element_counts[num] += 1
        # If the element is not in the OrderedDict, add it with a count of 1
        else:
            element_counts[num] = 1
    
    # Use a list comprehension to filter out elements with a count greater than 1
    unique_elements = [num for num, count in element_counts.items() if count == 1]
    
    return unique_elements

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```