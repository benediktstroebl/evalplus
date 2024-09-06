```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list.
    Result is a tuple of sum and product.
    If empty sum should be equal to 0, and empty product should be 1.

    >>> numbers = [5, 15, 10]
    return (sum(numbers), product(numbers))
    """

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

numbers = [5, 15, 10]
print(sum_product(numbers))  # This will print (30, 502105)
```