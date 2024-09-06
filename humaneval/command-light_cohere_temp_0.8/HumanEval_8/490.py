```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    return: (sum, product)
    """
    if not numbers:
        return (0, 1)
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append([5, 6, 7, 8])
test_sum_product.append([9, 9, 10, 11])
test_sum_product.append([12, 13, 14, 15])

# Function call and verify results
assert sum_product(*test_sum_product) == (15, 720)
```