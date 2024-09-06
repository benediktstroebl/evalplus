```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute the range.")
    mn, mx = min(numbers), max(numbers)
    return [(x - mn) / (mx - mn) for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. It first checks if the input list has at least two elements, raising a `ValueError` otherwise. It then finds the minimum and maximum values in the list using the `min` and `max` functions, respectively. Finally, it applies a linear transformation to each element in the list by subtracting the minimum value, dividing by the difference between the maximum and minimum values, and returning the modified list. 

Here is a simple test case to ensure the function behaves as expected:
```python
test_rescale_to_unit = {
    "test_simple_case": [
        "Function returns expected output for a list of numbers.",
        {"input": [1.0, 2.0, 3.0, 4.0, 5.0], "expected": [0.0, 0.25, 0.5, 0.75, 1.0]},
        rescale_to_unit
    ]
}
```