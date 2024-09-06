```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple (sum, product) where sum is the sum of all integers and product is the product of all integers.
    >>> numbers = [1, 2, 3, 4]
    return_sum_product = sum_product(numbers)
    print(return_sum_product)
    assert return_sum_product == (10, 24), "Test failed"
    return return_sum_product

numbers = [1, 2, 3, 4]
return_sum_product = sum_product(numbers)
print(return_sum_product)
```