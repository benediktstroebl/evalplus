```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
>>> sum_product([1, 2, 3, 4])
```

The code defines a function `sum_product` that calculates the sum and product of a list of integers. The function initializes variables for the product and sum to 1 and iterates through the input list, respectively multiplying the values and accumulating the sum.