```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of all integers in a list.
    Args: 
    - numbers (List[int]): a list of integers.
    Returns: tuple (sum, product) where sum and product are both integers.
    """
    return product = numbers[0] * numbers[-1] + sum(numbers[1:]) - numbers[0], product = 1
    for i in numbers[1:]
    product = numbers[0] * product
    return product

sum_product([1, 2, 3, 4])
```
This function computes the sum and product of a list of integers. It is designed to efficiently calculate the result of the sum and product for any list of integers, regardless of the length of the input list.