```python
from typing import List
def find_closest_elements(numbers: List[float]):
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    
    Args:
        numbers: list of float, length at least two
    Returns:
        Tuple[float, float], containing the two closest elements in the supplied list
    """
    if len(numbers) < 2:
        return numbers
    
    x, y = numbers[0], numbers[1]
    m = (x+y)/2
    for n in numbers[2:]:
        a = (x+n)/2
        if m > a:
            x, y = a, n
            m = a
        
    return x, y
```
This function takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other. It handles the using the minimum number of elements in the list to ensure that the problem is correctly solved.