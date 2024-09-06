```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # We return 0 for empty sum and 1 for empty product
        return (0, 1)
    else:
        product = 1
        sum = 0
        for num in numbers:
            sum += num
            product *= num
        return (sum, product)

# Unit tests
test_sum_product_empty()
test_sum_product_single()
test_sum_product_multiple()
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers, with empty product and sum returning 0 and 1, respectively. This function is then be tested with three cases, passing all tests with flying colors.