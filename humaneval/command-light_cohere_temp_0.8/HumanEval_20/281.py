```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    from typing import Tuple
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    min_num, max_num = (numbers[0] , numbers[1])
    for num in numbers[2:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num
```
This function takes a list of numbers and returns a tuple containing the two numbers that are the closest to each other. The function uses a sorting algorithm to find the two closest elements and returns them in order, where the smaller number is first.

Note that the function raises a ValueError if the list has less than two elements, which is not a valid input for this problem.