Here's a self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list,
    # such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    for n in numbers[1:]:
        n = ((n-numbers[0]) / (numbers[0] - 0)) * 1.0
   
   0)
    return numbers
```

This function takes a list of numbers as an argument and returns a list of the same numbers after applying a linear transformation. The function calculates the numbers[0] = 0 to ensure the smallest number is 0, then it calculates the rescaled numbers by dividing each number by the ratio of its difference from the smallest number and then multiplying by 1. The function returns the numbers as the final list.