Here is a self-contained Python script that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    min_num: float = float('inf')
    max_num: float = -float('inf')
    
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
            
    return (min_num, max_num)
```
This code defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest numbers. The function initializes two variables `min_num` and `max_num` to `float('inf')` and `-float('-inf')` respectively. It then iterates through each number in the list and checks if the current number is smaller than the current minimum or greater than the current maximum. If so, it updates the variable accordingly. Finally, the function returns the closest pair of numbers.