```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))

def products(numbers: List[int]) -> List[int]:
    result = 1
    for num in numbers:
        result *= num
    return [result]
```
This code defines two functions: sum_product and products. The sum_product function takes a list of integers as input and returns a tuple with the sum of the numbers and the product of all the numbers.

The products function is a helper function that computes the product of a list of integers. It uses a dynamic programming approach to compute the product by iterating through the list and multiplying each element.