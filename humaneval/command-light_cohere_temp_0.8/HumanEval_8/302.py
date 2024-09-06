```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Compute sum and product for a given list of integers.
    Return a tuple consisting of sum and product.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product = product * num
    product = product * sum
    return product, sum
    """

# unit test
numbers = [1, 2,3,4]
result = sum_product(numbers)
print(result)
```