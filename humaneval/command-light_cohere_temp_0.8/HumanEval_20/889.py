```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        return None

    numbers.sort()
    names = zip(numbers, numbers[1:])
    return_value = names[0][0], names[0][1]
```
This code defines a function called find_closest_elements that takes a list of numbers as input and returns a tuple with the two closest elements in the list, in order of their values. The code uses the sort function to sort the list of numbers, and then uses the zip function to create a tuple with the first and last elements of the sorted list. If the list of numbers is empty or has less than two elements, the function returns None.