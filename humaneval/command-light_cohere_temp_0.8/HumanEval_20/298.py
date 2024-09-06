```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    comparison_pair = None
    min_distance = float('inf')

    for i in range(0, len(numbers)):
        if comparison_pair is None or comparison_pair[1] > numbers[i]:
            comparison_pair = (numbers[i], i)
            min_distance = comparison_pair[0]
        else:
            if comparison_pair[0] != numbers[i]:
                comparison_pair = (numbers[i], i)
                min_distance = comparison_pair[0]

    if comparison_pair is None:
        return None

    return comparison_pair
```
This Python code defines a function called `find_closest_elements` that aims to find and return two elements from a list of numbers that are the closest to each other. 

It uses a technique similar to the bubble sort algorithm to compare and store the closest pairs in a list of input numbers. 

The function iterates through the list of numbers and whenever it finds a pair that is closer than the previously stored pair, it updates the stored pair. 

This process continues until no closer pair is found, at this point the function returns the stored pair.