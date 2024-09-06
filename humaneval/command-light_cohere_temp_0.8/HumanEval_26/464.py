```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    """
    list comprehension has through built-in function to check for duplicates and removes them.
    return a unique list of integers.
    """
    unique list of numbers after the duplicate removal"""
    numbers = set(numbers)  # converting set will remove duplicates
    return list(numbers)

# testing
test_remove_duplicates = [1, 2, 3, 2, 4, 2, 1, 5, 6]
test_remove_duplicates_result = remove_duplicates(test_remove_duplicates)
print(test_remove_duplicates_result)
``` 
This code defines a function called remove_duplicates, which takes a list of integers as input and returns a new list with duplicate numbers removed. The function uses a set to check for duplicates and then converts the set back to a list to get the unique elements. The function has been tested with a sample input and the result has been printed to the console.