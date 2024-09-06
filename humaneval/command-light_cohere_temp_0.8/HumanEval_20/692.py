Here's the self-contained Python script that solves the problem:
```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float]):
    # Using the Pythagorean distance formula
    d = (numbers[0] - numbers[1])**2
    return (numbers[0], numbers[1]) if d < (numbers[1] - numbers[0])**2 else (numbers[1], numbers[0])
```
This function takes a list of two numbers and returns a tuple of the two closest numbers in the list, it uses the Pythagorean distance formula to calculate the distance between the two numbers, and then selects the two numbers based on the smaller distance. The function then returns the the tuple in descending order.