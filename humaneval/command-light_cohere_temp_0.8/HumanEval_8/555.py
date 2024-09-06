```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    numbers = [1, 2, 3, 4, 5]
    sum, product = 0, 1
    for num in numbers:
        sum += num
        product *= num
    return sum, product
```