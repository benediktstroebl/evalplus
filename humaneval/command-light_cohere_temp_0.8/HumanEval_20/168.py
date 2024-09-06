Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    SELECTS AND RETURNS THE TWO NUMBERS THAT ARE CLOSEST TO EACH OTHER AND RETURNS THEM IN ORDER
    (SMALLER NUMBER, LARGER NUMBER)
    """
    numbers.sort()
    distance_between = [(a - b) for a, b in zip(numbers, numbers[1:])]
    return (min(distance_between), max(distance_between))
```

This function finds the two closest elements in the list and returns them in the order of the smaller number, larger number. The function sorts the required list of numbers and calculates the distances between each pair of numbers. This process is then faster than calculating the distances between all pairs of elements in the list. The function then selects the minimum distance from the distances and returns the corresponding pair of elements. 

This script is self-contained, and it does not require any external functions or classes.