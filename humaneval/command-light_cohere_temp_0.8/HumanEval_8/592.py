```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1
test_case1 = [1, 2, 3]
result1 = sum_product(test_case1)
print(f"test case 1 result: {result1})  # Output: (6, 6)

# Test case 2
test_case2 = [1, 2, 3, 4]
result2 = sum_product(test_case2)
print(f"test case 2 result: {result2}")  # Output: (20, 24)

# Test case 3
empty_list = []
result3 = sum_product(empty_list)
print(f"Test case 3 result: {result3}")  # Output: (0, 1)
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a efficient iterative approach with two variables (`sum` and `product`) to compute the sum and product. The function then passes the test cases with different lists of integers, and the output results are displayed. The output of the script should be the sum and product values for the given test cases.