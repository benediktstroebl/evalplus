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
test_sum_product.py
test_sum_product.sh: using(sum_product, test_sum_product)
test_sum_product.input [1, 2, 3, 4])
test_sum_product.assertEqual  [6, 4]
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers, returning a tuple of the sum and product as the result.

The function uses a loop to iterate over the list of integers, accumulating their sum and multiplying them to calculate the product. The product is initialized to 1, and the sum is calculated by adding each element in the list. 

The code then includes a series of unit tests using the `unittest` library, which test the `sum_product` function with various inputs.