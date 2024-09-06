Here is a self-contained Python script that solves the problem of finding the closest elements from a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    <return (closest_low, closest_high)>"""
    closest_low = float("inf")
    closest_high = float(-inf)
    for number in numbers:
        if closest_low > number:
            closest_low, closest_high = number, closest_high
        elif closest_high < number:
            closest_low, closest_high = number, closest_high

    return closest_low, closest_high
```

This function takes a list of numbers and returns a tuple containing the two numbers that are the closest to each other. It uses the specific values to represent the closest low and closest high numbers, and loops through the list of numbers, updating the closest low and closest high values as needed. The function returns the the closest low and closest high values.