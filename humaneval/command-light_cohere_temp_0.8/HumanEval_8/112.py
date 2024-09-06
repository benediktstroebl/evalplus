```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case for function
test_sum_product = []
test_sum_product.push_back(test_sum_product.push_back(0))
test_sum_product.push_back(1)
test_sum_product.push_back(2)
test_sum_product.push_back(3)
test_sum_product.push_back(4)

result = sum_product(test_sum_product)
print(f"Result: {result[0], result[1]}")
 ```