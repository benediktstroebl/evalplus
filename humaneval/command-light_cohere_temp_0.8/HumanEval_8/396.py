```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
sum_product_test_case_1 = [1, 2, 3]
sum_product_test_case_2 = [1, 2, 3, 4]
sum_product_test_case_3 = []

result_1 = sum_product(sum_product_test_case_1)
result_2 = sum_product(sum_product_test_case_2)
result_3 = sum_product(sum_product_test_case_3)

print(f"Test case 1 results: {result_1}")
print(f"Test case 2 results: {result_2}")
print(f"Test case 3 results: {result_3}")
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers, and passes these results as a tuple. It also includes a test cases, which are lists of integers, and the `sum_product` function is called on each test case to calculate the product of its elements. The results are then printed to the console.