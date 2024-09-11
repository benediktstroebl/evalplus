### Python Script to Remove Duplicate Elements in a List
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    List[int]: A new list with duplicate elements removed.
    """
    
    # Create an empty dictionary to store unique elements and their counts
    unique_elements = {}
    
    # Iterate over the input list to count the occurrences of each element
    for num in numbers:
        if num in unique_elements:
            unique_elements[num] += 1
        else:
            unique_elements[num] = 1
    
    # Create a new list to store the elements that occur only once
    result = []
    
    # Iterate over the input list again to add elements that occur only once to the result
    for num in numbers:
        if unique_elements[num] == 1:
            result.append(num)
    
    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input, counts the occurrences of each element, and returns a new list with duplicate elements removed. The function uses a dictionary to store the counts of each element and a new list to store the elements that occur only once. The order of elements in the result is preserved as in the input list.