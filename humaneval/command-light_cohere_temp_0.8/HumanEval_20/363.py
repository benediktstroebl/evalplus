Here is a self-contained Python script that solves the problem:

```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float]):
    """ 
    a,b = sorted((a,b) for a,b in zip(numbers))
    return (a,b) if len(a)<len(b) else (b,a)
```

This function takes a list of numbers as input and returns a tuple of the two closest elements. The function uses the sorting algorithm to sort the list of numbers based on their value, and then returns the two closest elements in order. This function can be used to solve the problem in a self-contained manner.