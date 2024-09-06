Here is the self-contained Python script that solves the problem of finding the closest elements from a list of floating-point numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).

    :return (smallest, largest)
    """
    if len(numbers) < 2:
        return (None, None)
    
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Determine the provider and distance
    provider, smallest = numbers[0]
    dist = 0
    for number in numbers[1:]:
        if number < provider:
            dist = 0
        else:
            dist = 1
        provider = number
    
    # Return the closest pair of numbers
    return (provider, dist)
```
This function accepts a list of numbers as an input and returns a tuple containing the smallest and largest number from the list, along with the associated distance. It will return (None, None) if the list contains only one number.