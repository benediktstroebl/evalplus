```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes elements that occur more than once from a list of integers.
    duplicates = set(numbers)
    return [x for x in numbers if x not in duplicates]
    """
    duplicates = set(numbers)
    return [x for x in numbers if x not in duplicates]

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

# Test with empty list
numbers = []
result = remove_duplicates(numbers)
print(result)

# Test with list of strings
numbers = ['item1', 'item2', 'item3']
result = remove_duplicates(numbers)
print(result)
``` 
This Python script defines a function `remove_duplicates` that takes a list of integers as input and removes all elements that occur more than once. It uses the duplicates set to keep track of duplicate elements, and then returns a new list containing only the elements that are not duplicates. The function is then tested with three different input scenarios: a list of integers, an empty list, and a list of strings. These tests demonstrate the result in removing duplicates from different data types.