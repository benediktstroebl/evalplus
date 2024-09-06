```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function
test_sum_product = sum_product([1, 2, 3, 4, 5]))
print(test_sum_product)  # Output: (15, 120)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. It also includes a type hint for `numbers` parameter using `List[int]`. The function returns a tuple of the sum and product. The test case uses the example `[1, 2, 3, 4, 5]` and prints the result (sum: 15 and product: 120).