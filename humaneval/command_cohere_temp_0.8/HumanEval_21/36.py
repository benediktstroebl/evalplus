```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute the range.")
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled from 0 to 1. The function first checks if the list has at least two elements using the `typing` module `List` annotation and raises a `ValueError` if it does not. It then determines the minimum and maximum values in the list using the `min` and `max` functions and calculates each value relative to the range between the minimum and maximum values.

Here's an example of using the `rescale_to_unit` function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(test_list))
```

The expected output for the input list `test_list` is:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
``` 

This indicates that the relative differences between the numbers in the original list are maintained, with the smallest value mapped to 0 and the largest value mapped to 1.