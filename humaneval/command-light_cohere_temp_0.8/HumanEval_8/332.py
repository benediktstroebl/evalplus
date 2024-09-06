```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))

def products(numbers: List[int]) -> List[int]:
    return [num * n for n, num in zip(numbers, numbers[1:])]
```
This script defines two functions: sum_product and products. The sum_product function takes a list of integers and returns a tuple of their sum and product, where the product is calculated by using the `products` function. The products function uses the value in the first element of a list and multiplies it to every element in the remaining list.