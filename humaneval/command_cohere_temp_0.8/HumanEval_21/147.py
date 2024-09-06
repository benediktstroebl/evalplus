```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This transformation is a linear transformation.

This code includes type annotations provided as a functionality of Python through the `typing` module. These annotations, like `List[float]`, provide additional clarity and ease of use for developers. 

The function is tested with the following markdown code block:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
```
Output: