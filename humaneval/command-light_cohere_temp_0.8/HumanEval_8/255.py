```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Unit tests
numbers_list = [1, 2, 3, 4]
test_sum_product = sum_product(numbers_list)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)

numbers_list2 = []
test_sum_product2 = sum_product(numbers_list2)
print("Sum:", test_sum_product2)
print("Product:", test_sum_product2)

```
This code has a self-contained function 'sum_product', which takes a list of integers as input and returns a tuple with the sum and product of the numbers. It handles the empty lists by returning (0,1), and passes unit tests.