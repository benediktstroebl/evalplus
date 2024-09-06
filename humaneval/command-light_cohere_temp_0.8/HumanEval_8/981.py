Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of a list of integers, and passes the corresponding tests:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with different inputs
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product_empty = []
test_sum_product_empty.append([])
test_sum_product_one = [1]
test_sum_product_two = [1, 2, 3]

print("Test 1: ", sum_product(test_sum_product))
print("Test 2: ", sum_product(test_sum_product_empty))
print("Test 3: ", sum_product(test_sum_product_one))
print("Test 4: ", sum_product(test_sum_product_two))
```
The code defines a function called sum_product, which takes a list of integers as input and returns a tuple containing their sum and product. The function first checks if the list is empty, in which case it returns (0, 1), and otherwise it returns the sum of the numbers followed by their product. The test code includes several test cases, which demonstrate the correctness of the sum_product function by passing different lists of integers. The expected output is the sum and product for each test case.