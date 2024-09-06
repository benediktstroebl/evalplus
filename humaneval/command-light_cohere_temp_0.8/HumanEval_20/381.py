Here is a self-contained Python script that solves the problem:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    # Select two numbers from the list that are closest to each other
    a, b = min(numbers[::a], numbers[::b])
    return a, b
```
This script defines a function called find_closest_elements, which takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other. The function uses the minimum function to find the smallest number in the list, and then uses the result to find the largest number in the list.