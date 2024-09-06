```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)
    # Get the first and second items of the sorted list
    first, second = numbers[:][0] , numbers[:][1]
    # Check the difference between the first and second numbers
    if first != second:
        # Return the difference
        return (first, second)
    # Return the closest elements in the list
    return (min(numbers), max(numbers))
```
This code will sort the list of numbers in ascending order and will return the first and second closest numbers in the list as a tuple, which is the solution for the problem.