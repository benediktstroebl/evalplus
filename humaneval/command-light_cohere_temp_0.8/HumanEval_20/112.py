```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    This function is designed to solve the problem of finding the closest pairs of elements in a list of numbers, and it does so using a simple tuple to return the results.
```
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

# Find the two closest elements:
# Sort the list of numbers
sorted_numbers = sorted(numbers)

# Find the two closest elements based on their value
closest_pair = tuple(sorted_numbers[0:2])

# Sort the elements of the pair by value
sorted_pair = sorted(sorted_pair)

return sorted_pair
```
The provided code defines a function called `find_closest_elements` that aims to solve the problem of finding the closest pairs of elements in a list of numbers. The function takes in a list of numbers as input and returns a tuple of the two closest elements in that list, with the smaller element first. The code first sorts the difference between the numbers in the list, and then uses the sorted list to find the two closest elements. Finally, the code sorts the elements of the pair by value and returns the tuple.