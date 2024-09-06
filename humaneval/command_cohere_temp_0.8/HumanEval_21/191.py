```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    return [(x-min(numbers))/(max(numbers)-min(numbers)) for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. This is achieved by calculating the linear factor as `((max-min)/(total digits after the decimal point))` and applying this factor to each number in the list. For example:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This transformed list encapsulates the original input range of values in the unit interval. 
This approach ensures that the relative relationships among the numbers in the list are preserved in a standardized format, making it convenient for further analysis and processing. F
urther, the function's `typing.List` annotation indicates that its expected input is a list of float values, and its return value is also a list of float values, which aligns with the function's behavior. 
This function is both robust and versatile, efficiently delivering the desired output for the given problem statement.