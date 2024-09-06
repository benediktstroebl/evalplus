Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float]):
    # select two closest elements
    elements = sorted((x, y) for x, y in zip(numbers[::2:]) + (numbers[0], numbers[1])), key= (x, y)>=>(sqrt(x)+sqrt(y))**0.5)
   2
    
    # Return the two elements in order
    return elements[0], elements[1]

# Test cases 
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

res = find_closest_elements(numbers)

print(res)
```
This script defines a function called `find_closest_elements`, which takes a list of numbers and returns a tuple of the two closest elements. The script uses the sorting algorithm with a custom key function to compare the elements and returns the two closest elements in the correct order.