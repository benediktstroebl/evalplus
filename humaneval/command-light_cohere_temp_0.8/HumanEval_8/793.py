Here is a self-contained Python function that solves the problem you provided:
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

This function takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. It iterates through loop throughs through each number and calculates both the product and sum at the same time.