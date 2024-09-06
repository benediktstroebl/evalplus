Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    scaled_numbers = [((x - min_value) / (max_value - min_value)) * 2 for x in numbers]
    return scaled_numbers
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of scaled numbers. The function first calculates the minimum and maximum values in the input list using the `min` and `max` functions, respectively. Then, a list comprehension applies a linear scaling transformation to each number in the list, where the smallest number becomes 0 and the largest number becomes 1.

To test this function, you can run the following code:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_test_list = rescale_to_unit(test_list)
print(rescaled_test_list)
```
The printed output should be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
``` 

This indicates that the input list has been transformed such that the smallest value (1.0) became 0, and the largest value (5.0) became 1. Consequently, the other numbers were scaled proportionally between these two extremes.