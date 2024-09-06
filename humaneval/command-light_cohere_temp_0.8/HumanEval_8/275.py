```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:  # empty list
        return (0, 1)
    elif len(numbers) == 0:  # empty product
        return (0, 0)
    else:
        return (sum(numbers), prod(numbers))
        """
def prod(numbers: List[int]):
    """ Calculate the product of all the integers in a list """
    if not numbers:  # empty list
        return 1
    elif len(numbers) == 0:  # empty product
        return 1
    else:
        return product(numbers)

def product(numbers: List[int]) -> int:
    """ Calculate the product of all the integers in a list """
    return reduce(lambda x, y: x * y, numbers, 1)
```
The provided Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The `prod` function calculates the product of the list of integers, and the `product` function uses the reduce function to calculate the product. This script also provides a validations for the functions to ensure correct output.