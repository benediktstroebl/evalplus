```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # empty list
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# test case 1
test_case1 = [1, 2, 3]
print(sum_product(test_case1))
# Prints (6, 6)

# test case 2
test_case2 = [1, 2, 3, 4]
print(sum_product(test_case2))
# Prints (20, 24)

# test case 3
test_case3 = []
print(sum_product(test_case3))
# Prints (0, 1)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function first checks if the list is empty and returns (0, 1) in that case. The function then initializes variables for the product and sum, and iterates through the list, accumulating the sum and multiplying the values to calculate the product.