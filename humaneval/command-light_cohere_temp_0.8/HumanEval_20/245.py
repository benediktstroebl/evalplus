```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Return the first and second element of the sorted list
    first, second = sorted_numbers[0], sorted_numbers[1]
    return first, second
``` 

This Python function, `find_closest_elements`, is defined to find and return the two closest elements in a list of numbers. The function takes in a list of numbers as an argument and sorts the list in ascending order using the `sorted` function. The first and second elements of the sorted list are then returned and returned in that order.

The function can be tested by calling it with a sample list of numbers, and the returned tuple can be used to access the two closest elements in the list. 

This function demonstrates the use of the `sorted` function to sort a list of numbers and the ability to extract and return the two closest elements from that sorted list.