Here is a self-contained Python script that solves the problem of calculating the sum and product of integers in a list:

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

test_sum_product = []
test_sum_product.push_one(10)
test_sum_product.push_two(2)
test_sum_product.push_three(3)
test_sum_product.push_four(4)

print(sum_product(test_sum_product))
print(test_sum_product[0] * test_sum_product[1])
```

In this script, the function sum_product calculates the sum and product of integers in a list. The function first checks if the list is empty, and returns (0, 1) in such cases. If the list is not empty, it returns the sum of the list and the product of the list.

The test_sum_product list contains a series of test cases. The test cases are executed by calling the sum_product function with each test case, and the results are then printed.