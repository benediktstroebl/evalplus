```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Find the two closest elements
    first, second = (numbers[0], numbers[1])
    while len(numbers) > 1:
        current = (numbers[0], numbers[1])
        if current < first:
            first, second = current
        elif current > second:
            first, second = current
    return first, second
``` 
This code defines a function called `find_closest_elements` that takes a list of numbers as an argument and returns a tuple of the two closest numbers. 

It sorts the list of numbers and then iteratively finds the two closest elements by comparing them and swapping if necessary. 

The code is designed to efficiently find the closest pairs of elements in a list, which is useful for a variety of data analysis tasks.