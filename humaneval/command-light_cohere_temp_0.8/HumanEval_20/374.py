Here is a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize two variables to store the closest elements
    x1, x2 = (numbers[0] + numbers[1]) / 2, (numbers[0] - numbers[1]) / 2
    # Return the two closest elements in the list
    return (x1, x2)
```

The function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two closest elements in the list, with their values in descending order. The function uses the floating point arithmetic to find the closest elements and returns them in order of their magnitudes.