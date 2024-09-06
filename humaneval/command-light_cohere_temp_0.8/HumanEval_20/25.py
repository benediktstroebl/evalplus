```python
from typing import List
def find_closest_elements(numbers: List[float]):
    x, y = (min(numbers), max(numbers))
    return x, y
``` 
This Python function, named find_closest_elements, takes a List[float] parameter representing an array of numbers. It uses the lowest and maximum values from the numbers list to calculate the closest elements, returning them in that order. This method is designed to efficiently find the two closest elements in the array.