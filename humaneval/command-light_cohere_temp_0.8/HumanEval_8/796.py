```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return result, product
# Test cases
test_sum_product_inputs = [1, 2, 3, 4]
test_sum_product_expected = [3, 12]

test_empty_inputs = []
test_empty_expected = (0, 1)

print(sum_product(test_sum_product_inputs)) # expected output: 3
print(sum_product(test_sum_product_inputs)[[1]) # should be error, as list is empty
print(sum_product(test_empty_inputs)) # expected output: 0
print(sum_product_empty_expected) # expected output: (0, 1)
```