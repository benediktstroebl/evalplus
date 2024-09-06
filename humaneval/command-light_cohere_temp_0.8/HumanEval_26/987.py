```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list and return the unique elements in order.
    """
    unique elements = set(numbers)
    return list(unique_elements)
    """
    return [num for num in unique_elements]
 
# Test case
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
``` 
This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. It uses the unique element method to convert the input list into a set, then converts it back to a list. This ensures that the elements that appear more than once are removed from the list.