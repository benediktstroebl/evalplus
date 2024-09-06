```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    return [(x-min(numbers))/(max(numbers)-min(numbers)) for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. The intermediate numbers are linearly scaled between 0 and 1. The transformation is achieved by calculating the difference between each number in the list and the minimum of the list, and then dividing it by the difference between the maximum and minimum of the list. This ensures that the relative relationships among the numbers remain intact while mapping the range of values to between 0 and 1. 

To ensure that the function handles the edge case where the input list contains only one element or is empty, thereby raising an `ValueError`, we can modify the function as follows: 
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers or len(numbers) == 1:
        raise ValueError("Input list must have at least two elements")

    return [(x-min(numbers))/(max(numbers)-min(numbers)) for x in numbers]
``` 

This modified function raises a `ValueError` when the input list has less than two elements, or is empty. 

The function's docstring explains the purpose and behavior of the function, and exemplifies its usage. The resulting list of rescaled numbers achieves the desired range adjustment through linear transformation, preserving relative relationships among the numbers. 

You can utilize this function to rescale lists of numerical data for various analysis, visualization, or normalization purposes, ensuring that the output falls within the convenient range of 0 to 1.