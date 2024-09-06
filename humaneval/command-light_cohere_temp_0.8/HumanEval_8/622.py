```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_data = [1, 2, 3, 4]
test_results = sum_product(test_data)
print("Test Results:", test_results)

numbers = []
numbers. empty_result = sum_product(numbers)
print("Empty List:", empty_result)

numbers = [1, 2, 3]
single_product_result = sum_product(numbers)
print("Single Product:", single_product_result)

large_numbers = [21, 42, 7]
large_sum_product = sum_product(large_numbers)
print("Large Sum Product:", large_sum_product)
```