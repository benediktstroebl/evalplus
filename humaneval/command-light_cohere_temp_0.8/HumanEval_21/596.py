```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Input:
    numbers: The list of numbers to be rescaled
    
    Output:
    rescaled_numbers: The list of numbers after applying the transformation
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    rescaled_numbers = [0.0] + numbers[rescale_to_unit(numbers[1:]))
    for n in numbers[1:]:
        rescaled_numbers.append(n * (1.0, rescaled_numbers[-1] * n)
    return rescaled_numbers
```

This Python function named `rescale_to_unit` is designed to transform a given list of numbers in such a way that the smallest value becomes 0 and the largest value becomes 1. 

The function first checks whether the input list has at least two elements. If it doesn't, it raises a `ValueError` with an appropriate error message.

The function then initializes a new list `rescaled_numbers` with the first number in the input list set to 0. It then uses list comprehension to create a new list `numbers_rescale` by applying the transformation to each element in `numbers` and then applies the same transformation to each element in `numbers_rescale` using element-wise multiplication and the original transformation.

Finally, the function returns the `rescaled_numbers` list, which contains the numbers after applying the desired transformation.