Here is a self-contained Python script that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Return 0 and 1 if an empty list is passed
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]) -> int:
    result = 1
    for num in numbers:
        result *= num
    return result
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The `products` function is used to calculate the product of all the integers in the list.