Here is a Python function that can be used to solve the problem and pass the test:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Initialize scaling factors
    scaling_factors = [1.0] + [maximum(numbers[0] - numbers[1])] / (numbers[1] - numbers[0])

    # Apply scaling factors to the list and return the result
    return [scaling_factors[i] * num for i, num in enumerate(numbers)]

# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = rescale_to_unit(numbers)
``` 
Do you need anything else?