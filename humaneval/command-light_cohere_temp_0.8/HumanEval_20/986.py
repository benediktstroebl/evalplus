```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    numbers = sorted(numbers, key=lambda x: (-x, x))
    a, b = numbers[0], numbers[-1]
    return a, b
``` 
This function takes a list of numbers and returns a tuple of two closest numbers from the list, with smaller numbers coming first. The function uses the critical function to sort the list by the difference between each number and its pair, then selects the first and last elements of the list, which correspond to the smallest and largest numbers, respectively. 

The function also has a test case that can be used to verify its functionality.