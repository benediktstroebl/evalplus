Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num
    return (sum_result, product_result)

# Test the function
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print(test_result)  # Output: (10, 24)

# Test the function with empty data
empty_data = []
empty_result = sum_product(empty_data)
print(empty_result)  # Output: (0, 1)
```
This code defines a `sum_product` function that calculates the sum and product of a list of integers. The `sum_product` function returns a tuple containing the sum and product of the numbers in the list. The code also provides two tests of the function: one with a list of integers and another with an empty list.