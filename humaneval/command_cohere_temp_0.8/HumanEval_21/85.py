```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. This is achieved by calculating the minimum and maximum values in the input list, and applying a linear transformation to the numbers, using these parameters as normalization coefficients. This is a common technique to make numerical values lie between 0 and 1, which is especially useful for machine learning or visualization. 

To validate the functionality of the function, below is a Markdown code block with a simple test case using the `pytest` framework, which should pass with the provided function:
```python
pytest -v test.py
```