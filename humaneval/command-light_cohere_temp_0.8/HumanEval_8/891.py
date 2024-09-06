```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
#unit tests
test_sum_product_list = [1, 2, 3, 4]
test_sum_product_result = sum_product(test_sum_product_list)
print("Test sum product results:", test_sum_product_result)
```