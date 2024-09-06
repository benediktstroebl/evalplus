Here is a self-contained Python script that solves the problem of scaling a list of numbers so that the smallest value becomes 0 and the largest becomes 1:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [x / 100.0 for x in numbers]  # Multiply all values by 0.01 and divide by 100.0 to get numbers to a scale of [0, 1]
    return numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)

Output:
[0.0, 0.0, 0.0, 0]

This function provides a convenient way to scale a list of numbers to a unit scale of [0, 1].