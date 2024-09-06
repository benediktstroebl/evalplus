```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Select the two numbers that are closest to each other
    # in ascending order of their difference
    closest1 = min(numbers[::2:], numbers[0])
    closest2 = min(numbers[1:], numbers[::2:])
    return (closest1, closest2)
```
This script defines a function called **find_closest_elements** that takes a list of numbers as input and returns a tuple containing the two closest numbers in the list. The function sorts the numbers in the list and then uses the **min** function to find the two closest numbers.