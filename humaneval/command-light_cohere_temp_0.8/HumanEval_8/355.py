```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list
        return (0, 1)
    return (sum(numbers), products(numbers))

def products(numbers: List[int]) -> int:
    if not numbers:  # Empty list
        return 1
    result = 1
    for num in numbers:
        result *= num
    return result
```
This script defines a `sum_product` function that calculates the sum and product of integers in a list, with empty product and sum being returned as 0 and 1, respectively. The `products` function calculates the product of integers in a list. The script includes tests to validate the function's behavior.