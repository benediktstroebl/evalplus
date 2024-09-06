Here's a Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # the list must be of length at least two
    a, b = (min(numbers[0], numbers[1]) for i in range(2))
    closest = numbers[0] < numbers[1] and a == numbers[0]
    closest = min(numbers[0], numbers[1])
    return a, b
```

This code defines a function called `find_closest_elements` that takes a list of numbers as an input and returns a tuple of the two closest numbers in the list.

The function uses the `min` function to compare the two numbers and returns the smaller one. The function then uses the `if` statement to compare the smallest number with the second number and returns the second number.