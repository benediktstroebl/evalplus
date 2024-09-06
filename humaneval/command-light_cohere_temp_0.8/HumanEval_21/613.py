Here's the solution to the markdown code block problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers[0] = 0  # Set the first element to 0
    numbers = [x * (-1.0) for x in numbers] + [x * 1.0 for x in numbers]  # Apply the linear transform to each number in the list
    return numbers
```

The function `rescale_to_unit` takes a list of numbers and returns a list of the same numbers but with the applied linear transformation. The function works by first setting the first element of the input list to 0, then applying a linear transformation to each subsequent element by multiplying it by -1 and adding 1.