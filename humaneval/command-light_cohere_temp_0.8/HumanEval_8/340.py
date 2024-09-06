```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # empty list test
        return (0, 1)
    return (sum(numbers), products(numbers))

def products(numbers: List[int]) -> List[int]:
    result = 1
    for num in numbers:
        result *= num
    return [result]
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It utilizes other helper functions, `products` and checks for an empty list, returning a default value of `(0, 1)`. This function can be used to compute the sum and product of any list of integers.