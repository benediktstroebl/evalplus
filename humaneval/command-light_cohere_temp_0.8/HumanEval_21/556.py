Here's a self-contained Python script that solves the problem of scaling numbers between 0 and 100:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number becomes 0 and the largest becomes 1."""
    numbers.extend(x / (100.0 - min(numbers) + 1e - min(numbers)))
    return numbers

```

This function rescales the input list of numbers to a unit where the smallest value is 0 and the largest value is 1, by applying a linear transformation. It achieves this by calculating the formula, which scales the numbers to the unit range [0, 100] while keeping the relative order and smallest value at 0.