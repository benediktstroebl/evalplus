Here is a self-contained Python script that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ A utility function to calculate the sum and product of a list of integers. """
    
    if not numbers:  # Empty list case
        return (0, 1)
    else:  
        return (sum(numbers), products(numbers))

def products(numbers: List[int]) -> List[int]:
    """ A helper function to calculate the product of a list of integers"""
    result = 1
    for num in numbers:
        result *= num
    return [result]
```

This script defines two functions, `sum_product` and `products`, to calculate the sum and product of a list of integers, respectively. For the `sum_product` function, if the input is an empty list, it returns a tuple of 0 and 1. If the list is not empty, it returns the sum of the list and the product of the list using the `products` function.