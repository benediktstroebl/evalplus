```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
print(result)  # Output: (6, 24)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function also implements a test case with the values [1, 2, 3, 4]. The output of the function is then printed, which should be (6, 24) in this case.