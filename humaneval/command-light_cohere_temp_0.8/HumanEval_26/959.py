Here is a self-contained Python script that solves the problem of removing duplicates from an input list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from a list of integers and return the unique elements.
    """
   
    list comprehension with set() is a common way to do this in Python.
    Unique elements = set(numbers)
    return [element for element in numbers if element not in Unique]
    """

# Test the function with sample input
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```
This script defines a remove_duplicates function that takes a list of integers as input and returns a new list with all unique (non- duplicate) elements from the input list. It uses the unique elements set to create a set of the input list elements and then uses the list comprehension to filter out elements that are in the unique set.