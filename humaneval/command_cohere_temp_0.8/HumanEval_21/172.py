Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    return rescaled
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled numbers based on the description of the problem. The linear transformation is performed using Python's list comprehension and subtraction, division, and max() functions.