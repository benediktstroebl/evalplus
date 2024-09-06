Here is a Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers.extend(numbers * [1.0 / min(numbers) + 1.0))
    = numbers.tolip(numbers)
   numbers = [num / 1.0 for num in numbers]
    return numbers
```

This function takes a list of numbers and applies a linear transform to that list, such that the smallest number will become 0 and the largest will become 1. It uses the function `min` to find the minimum value in the list and then divides each number in the list by this minimum value and the constant 1. The function then returns the numbers, which have been rescaled to the unit [0, 1].

This is a good start, but you might consider adding some tests to ensure the function works correctly with different inputs.