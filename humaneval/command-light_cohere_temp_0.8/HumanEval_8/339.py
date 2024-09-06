Here's the solution:
```python
from typing import List

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

The code defines two functions: `sum_product` takes a list of integers as input and returns a tuple with the sum and product of all integers in the list. The `products` function computes the product of all integers in the list.