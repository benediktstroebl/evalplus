```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers rescaled to the range between 0 and 1 (inclusive). The transformation is a linear transformation that is applied to all numbers in the list.

The function first finds the minimum and maximum values of the input list using the `min` and `max` functions, respectively. Then, for each number in the list, it subtracts the minimum value, divides by the difference between the maximum and the minimum values, and multiplies by 1 to get the desired transformation.

Here is an example of using the function with a test case that verifies if the output is as expected:
```python
rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
#[0.0, 0.25, 0.5, 0.75, 1.0]
```