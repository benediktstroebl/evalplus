Here's a self-contained Python function that solves the problem:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = []
test_numbers = [1, 2, 3, 4]
test_sum_product.check_sum_product(test_numbers)
```

This function calculates the sum and product of the integers in a given list, following the docstring you provided. The function is then passed to the test_sum_product list, which contains the input test data. The function will return a result, which is then checked to see if it is correct.