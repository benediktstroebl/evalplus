Here is a Python script that implements the `find_closest_elements` function:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two closest elements from the input list """
    min_dist = float('inf')
    closest_num = None
    for num in numbers:
        current_dist = abs(num - closest_num)
        if current_dist < min_dist:
            min_dist = current_dist
            closest_num = num
    return closest_num, min_dist
```
This script defines a function that takes a list of numbers as input and returns a tuple with the two closest elements from the list and their distance. The function uses a mathematical operation `abs()` to calculate the absolute difference between the current number and the number that is currently the closest element.