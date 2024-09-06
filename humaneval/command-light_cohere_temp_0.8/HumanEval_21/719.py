Here is a Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [num / (max(numbers) + 1e) for num in numbers]
    return numbers
```

This code defines a function called rescale_to_unit, which takes in a list of numbers and returns a new list where each number has been rescaled to be between 0 and 1. The rescale is done using the formula (num / (max(numbers) + 1e)) which divides each number by the maximum number plus 1 to ensure the range is between 0 and 1. The division is performed by taking the absolute maximum of the numbers in the list to ensure that the largest number is not lost in the division.