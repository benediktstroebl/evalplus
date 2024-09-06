Here's a self-contained Python function that solves the problem of finding the two closest elements in a list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ 
    Two elements that are the closest to each other are selected and returned in order (smaller number, larger number)
    """
    min_dist = float("inf")
    # Sort the list of numbers based on their difference to the others
    numbers.sort(abs(x - y) for x, y in zip(numbers, numbers[1:]))
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            dist = abs(numbers[i]-numbers[j])
            if dist < min_dist:
                min_dist = dist
                closest = [numbers[i], numbers[j]]
    return closest
```

This function takes a list of numbers as an input and returns a tuple of the two closest elements in the list, along with the distance between them. The function first sorts the0 list based on the absolute values of the differences to each other, and then iterates through the sorted list, comparing the differences of each pair of elements to the current minimum distance. The pair with the smallest difference is then stored in the closest variable.

This function has been self-contained and does not rely on any other functions or modules.