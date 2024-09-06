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

The function `rescale_to_unit` ensures that the list meets the requirement of having at least two numbers, using `ValueError` for any input with less than two numbers, prompting the user for a valid input. It then calculates the minimum and maximum values in the list and divides each element by the range of the values (`max_value - min_value`) to guarantee that the smallest becomes 0 and the largest becomes 1.

Here is an example of function usage:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(test_list))
```

The function can be correctly called with the example list, and it will return the modified list with the scale applied:
```bash
[0.0, 0.25, 0.5, 0.75, 1.0]
``` 

This is the expected outcome, with the smallest number (1) scaled down to 0 and the largest number (5) scaled up to 1.