Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list
        return (0, 1)
    sum_product = (sum(numbers), products(numbers))
    return (sum(numbers), products(numbers))


def products(numbers: List[int]) -> List[int]:
    result = 1
    for num in numbers:
        result *= num
    return result
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The `products` helper function multiplies all elements in the input list to produce a product.

It returns a tuple with two values: the sum of the list and the product of the list.

You can test the function by calling it with different lists of integers and verify that the output is correct.