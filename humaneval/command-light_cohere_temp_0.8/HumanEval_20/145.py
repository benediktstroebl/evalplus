Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    Lower limit
    min = float('inf')
    max = 0
    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
        if numbers[i] > max:
            max = numbers[i]
    closest_num, closest_denominator = max, 1
    return (closest_num, closest_denominator)
```

This script defines a function find_closest_elements that takes a list of numbers as an argument and returns a tuple containing the two closest numbers and their common denominator. The script uses a time to iterate through the list of numbers, comparing each number to the current maximum and minimum values. The maximum and minimum values are then updated and stored in the closest_num and closest_denominator variables. The script then returns the maximum and minimum values in a tuple, which is then returned by the function.