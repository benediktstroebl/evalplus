```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple (sum, product) where sum is the sum of numbers and product is the product of all the numbers in a list."""
    if not numbers:
        return (0, 1)
    sum_ = 0
    prod_ = 1
    for num in numbers:
        sum_ += num
        prod_ *= num
    return (sum_, prod_)
# Test the function with valid inputs
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
assert result == (5, 12)
```