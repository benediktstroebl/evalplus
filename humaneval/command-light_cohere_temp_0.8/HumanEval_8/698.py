Here is a self-contained Python script that includes a function sum_product, which accepts a list of integers and returns a tuple containing their sum and product:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> sum_product([])
    () -> ()
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```