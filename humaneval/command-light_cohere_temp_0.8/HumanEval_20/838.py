Here is the solution:

```python
from typing import List
from math import at

def find_closest_elements(numbers: List[float]):
    """ Selects the two closest elements in the list, and returns them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] -- list of numbers

    Returns:
        Tuple[float, float] -- tuple of two closest elements
    """
    numbers = list(set(numbers))  # remove duplicates
    numbers.sort(reverse=True)  # sort in descending order
    smallest, largest = float("inf"), float(-inf)
    for i in range(len(numbers) - 1):
        if numbers[i] < smallest and numbers[i] > largest:
            smallest, largest = numbers[i], numbers[i+1]
    return smallest, largest
```

This function will return a tuple of two numbers that are the two closest to each other in the list, and the order will be the same as you provide.  You target: [1.0, 2.0, 3.0, 4], which2].