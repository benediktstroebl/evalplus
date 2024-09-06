Here is a Python script that implements the find_closest_elements function, which takes a list of numbers and returns a tuple of two closest numbers in the list, along with a boolean indicating which pair is closer:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort_keys, numbers
    keys = sorted(numbers, key=lambda x: x, reverse=True)
    
    # The first two numbers in the sorted list are the closest
    first, second = numbers[0], numbers[1]
    closest = (first, second)
    
    return closest

```

The script implements a solution to the problem of finding two closest elements in a list of numbers. The solution is a simple one, but it can be modified to handle more complex problems.