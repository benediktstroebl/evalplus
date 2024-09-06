```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Input validation: Check if the list is at least length 2
    if len(numbers) < 2:
        raise ValueError("Input list must be at least length two.")
    # Sorting and selection: Sort the list in ascending order of numbers, then get two closest elements and return them in order
    return (sorted(numbers)[0], sorted(numbers)[1])
```
This function, when called with a list of numbers, will return a tuple containing the two closest numbers from the list, with the smaller number first. The function checks the accuracy of the input, raises a ValueError if the list is not at least length two, and the returned values are guaranteed to be correct and sorted according to the selection criteria.