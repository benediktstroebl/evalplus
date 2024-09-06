```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in the list.
    """
    empty sum is equal to 0, and empty product is 1.
    product = 1
   
    for num in numbers:
        product *= num
    return product, sum(numbers)
```