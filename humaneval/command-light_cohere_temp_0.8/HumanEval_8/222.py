Here's the self-contained Python script that implements the function `sum_product` from the previous prompt:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a given list.
    Args:
    numbers (List[int]): a list of integers
    Returns:
    (sum, product) (int, int): a tuple containing the sum and product of all the integers in the list.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```
This script defines a `sum_product` function that takes a list of integers as an argument and returns a tuple containing the sum and product of the numbers in the list. It uses a straightforward iteration to add up the numbers and multiply them to compute the product.