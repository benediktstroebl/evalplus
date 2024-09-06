Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)"""
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Get the indices of the first two elements in the sorted list
    index_1 = 0
    index_2 = 1
    
    # Get the two closest elements in the sorted list
    first_element = sorted_numbers[index_1]
    second_element = sorted_numbers[index_2]
    
    return first_element, second_element
```
This function, `find_closest_elements`, takes a list of numbers as an input and returns a tuple containing the two closest elements. The function sorts the two closest elements based on the values of the list and returns them in that order. It uses the Python's sorted() function to sort the list of numbers and uses the indices of the first two elements in the sorted list to get the desired elements.