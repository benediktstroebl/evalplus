Here is a Python script that contains a self-contained function that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Use tuple unpacking to create a new tuple with the two closest numbers.
    closest = Tuple(sorted(numbers, key=lambda num: (num, num)))
    return closest

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = find_closest_elements(numbers)
```

In this script, the function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two numbers that are the closest to each other. The function sorts the numbers using the key function, which returns a tuple containing the two numbers that are the closest to each other.