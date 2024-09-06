```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of integers in a list.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Test cases
test_sum_product = [1, 2, 3, 4]
test_sum_product_empty = []

result_test_sum_product = sum_product(test_sum_product)
result_test_sum_product_empty = sum_product([])

print("Test case 1 result:", result_test_sum_product)
print("Test case 1 expected:", (10, 24))")

result_test_sum_product_empty = sum_product_empty()
print("Test case 2 result:", result_test_sum_product_empty)
print("Test case 2 expected:", 0)
```
The script defines a function sum_product that calculates the sum and product of a list of integers. The function then passes tests using a test case with a sample list of integers and an empty list, respectively. The function returns the expected values for these test cases.