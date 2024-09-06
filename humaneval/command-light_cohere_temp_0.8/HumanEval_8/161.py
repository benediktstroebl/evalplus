```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    Product is calculated using the maximum number in the list and then multiplying all other numbers.
    Sum is calculated using a difference between maximum and minimum numbers and then summing all other numbers.
    Returns a maximum product as a tuple of sum and product values.
    """
    
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (10, 24)
    """
    product = numbers[0]
    for num in numbers[1:]:
        product *= num
    sum = numbers[0] + (product - 1) + (sum - product)
    return (sum, product)
```