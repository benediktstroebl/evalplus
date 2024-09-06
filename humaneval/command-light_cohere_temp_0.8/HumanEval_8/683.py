Here's a self-contained Python function that solves the problem of calculating sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```

This function takes a list of integers as input and returns a tuple with two values: the sum of the numbers in the list and the product of all the numbers.