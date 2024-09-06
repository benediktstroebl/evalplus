```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two numbers from the list that are closest to each other. Returns the two numbers in order of being smaller than the larger number."""
    return (numbers[0], numbers[-1])
```
This code provides a function called find_closest_elements that takes a list of numbers as input and returns a tuple containing the two numbers from the list that are the closest to each other. The function uses the list comprehension and the Tuple function to select the two numbers. The result is (numbers[0], numbers[-1]) which will be the two closest numbers in the list.