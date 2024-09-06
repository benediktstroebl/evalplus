```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case: empty list returns (0, 1)
test_empty = sum_product([])
print(test_empty)
# Test case: list with integers returns (sum, product)
test_normal = sum_product([1, 2, 3, 4])
print(test_normal)
``` 
This script provides a self-contained function `sum_product` that calculates the sum and product of a given list of integers, passing corresponding tests.  It ensures type and can be easily used and understood in larger codebases without depending on external implementations or requirements.