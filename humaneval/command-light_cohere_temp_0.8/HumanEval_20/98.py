Here is a self-contained Python script that solves the problem of finding the two closest elements in a list of floating-point numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]) -> List[Tuple[float, float]]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    closest1 = float('inf')
    closest2 = float('-inf')
    for num in numbers:
        if num < closest1:
            closest1 = num
        if num < closest2:
            closest2 = num
    return [(closest1, closest2)]
```

This function takes a list of numbers and returns a list of tuples, where each tuple contains the two closest numbers to each other in the list, in order of their magnitude. The function also assigns the numbers in the list that are smaller than the current closest pair as the new closest pair.