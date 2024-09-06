```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select the two closest elements and return them in order
    closest1 = min(numbers)
    closest2 = max(numbers)
    numbers.remove(closest1)
    numbers.remove(closest2)
    # Return the first and second closest elements
    return (closest1, closest2)
```
This function takes a list of numbers and returns a tuple of two closest numbers in the list, in order of them being smaller. The function uses the simple min and max functions to select the closest elements, and then removes them from the list to ensure that the result is correct.