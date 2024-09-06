Here is the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Select the first and second elements of the sorted list
    first, second = sorted_numbers[0:1]
    # Return the two elements in the same order as before
    return first, second
```
The provided code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers from the input list. 

This is achieved by sorting the input list of numbers and then selecting the first and second elements of the sorted list, which correspond to the two closest numbers.

The function then returns the two elements in the same order as before, which is the desired behavior to solve the problem of finding the closest pairs of elements in a list of numbers.