Here's a self-contained Python script that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)"""
    numbers.sort(num for num in numbers if num < numbers[0])
    return (numbers[0], numbers[1])
```
This function takes a list of numbers as input and sorts the list based on the numbers being smaller to the left and larger numbers to the right. The function then returns the two closest numbers in the list and returns them in order.