```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers)) * 1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. The transformation is a linear normalization that scales the numbers between the minimum and maximum values of the input list.

To achieve this, it calculates the minimum and maximum values of the input list using the `min` and `max` functions, respectively. Then, for each number `x` in the input list, it applies the linear transformation formula: `(x - min)/(max - min) * 1`. This formula subtracts the minimum value, divides by the difference between the maximum and minimum values, and then multiplies by 1 to scale the numbers between 0 and 1.

The returned list is a normalized version of the input list, with values ranging between 0 and 1.

Here is an example of using the above function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)
print(result)
```

The output will be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This indicates that the original list has been transformed so that the smallest value (1.0) is now 0, and the largest value (5.0) is now 1. All other values have been scaled proportionally between these two extremes. 

The function assumes that the list contains at least two elements; this is technically necessary for the computation to be well-defined, as division by zero would otherwise occur if the list had only one element.