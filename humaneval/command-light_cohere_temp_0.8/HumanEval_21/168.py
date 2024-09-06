```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers list
    numbers_res = [x / (x + 1) for x in numbers]
    return numbers_res

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)
```
This script defines a function `rescale_to_unit` that takes a list of numbers as an argument and returns a new list where each element is the corresponding value divided by the sum of the elements plus one. The function achieves this goal by applying a linear transformation to the input list, which scales the numbers so that they range from 0 to 1.