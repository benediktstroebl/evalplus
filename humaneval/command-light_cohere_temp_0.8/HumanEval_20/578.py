```python
from typing import List
def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple of two numbers from the list that are the closest to each other and in order of their magnitude.
    numbers = sorted(numbers, reverse=True)
    smaller, larger = (numbers[0], numbers[-1])
    return smaller, larger
```
This function takes a list of numbers and returns a tuple of the two closest elements in the list. The function also tests the test to be passed the test with a List[float] as the numbers parameter and returns a tuple of the two closest elements.