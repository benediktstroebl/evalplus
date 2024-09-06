```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [n / max(numbers) for n in numbers]
    return [x * max(numbers) + 0.0 for x in numbers]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the elements of the input list rescaled to the range [0, 1]. The function uses the `List` and `float` data types and the `max` function to determine the maximum element in the list. It then divides each number in the list by the maximum number and then multiplies the result by -1 to convert it to the range [0, 1]. The Finally, the function returns the list with the rescaled numbers.