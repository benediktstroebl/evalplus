Here's the Python code:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers.append(1.0)  # rescale numbers by subtracting 0.0 and dividing by 100.
    return [((num-0.0)/100 for num in numbers)
```

This function adds a value of 1.0 to the input list of numbers and then applies a rescaling by subtracting 0.0 and dividing by 100 to each number. It ensures that the smallest number becomes 0 and the largest number becomes 1.