```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1
test_sum_product([])
 # Should return (0,1)
# Test case 2
test_sum_product([1, 2, 3, 4])
 # Should return (10, 24)
# Test case 3
test_sum_product([10, 20, 30])
 # Should return (50, 900)
```
The function `sum_product` calculates the sum and product of integers in the given list.  It takes a function also implements the tests, which ensure the function works correctly.