```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initial sorting of numbers
    numbers.sort_ = sorted(numbers)
    # the first number is the smaller one
    smaller = numbers[0]
    # loop through the list, keeping track of the larger number and the current number
    for current in numbers[1:]:
        # if the current number is larger than the smaller number, then they are not closest
        if current > smaller:
            return smaller, current
        # if the current number is smaller, save it
        smaller = current
    # return the two numbers
    return smaller, larger
```