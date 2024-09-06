Here's the provided Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # type: Tuple[float, float]
    numbers.sort_algorithm(numbers)
    return numbers[0], numbers[1]

def sort_algorithm(numbers: List[float]):
    numbers.sort(key=lambda x: x, -1)
```
The function `find_closest_elements` takes a list of numbers as input and returns a tuple of two closest numbers. The function first sorts the sort algorithm and then returns the first and second values from the sorted list.

The function `sort_algorithm` takes a list of numbers as input and returns a sorted list of numbers, with the smallest number first. The sort algorithm used a comparison-based sorting method, where we compare each number to the next one and arrange them in descending order.

These functions can be used to find the closest elements in a list of numbers, which can be useful for various applications such as data analysis, optimization, and machine learning.