Here's the code:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns the two closest elements in the list and their order """
    numbers.sort()
    smallest = sorted(numbers, key=lambda x: x[0])
    largest = sorted(numbers, key=lambda x: x[1])
    return (smallest, largest)
```
The `find_closest_elements` function takes a list of numbers as input and returns a tuple containing the two closest elements in the list, along with their order. The function sorts the of the numbers based on the first and second values, respectively. Using this, the smallest value is determined to be the smaller value, and the largest value is determined to be the larger value. The function then returns a smallest value and the largest value, respectively, in the order that they were sorted.