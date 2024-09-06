```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_sum_product_list = [1, 2, 3, 4]
test_sum_product_tuple = (10, 20)
test_empty = ()
test_one = [1]

print("Test cases:")
print(sum_product(test_sum_product_list))  # Output: (10, 120)
print(sum_product(test_sum_product_tuple))  # Output: (30, 2040)
print(sum_product(test_empty))  # Output: (0, 1)
print(sum_product(test_one))  # Output: (1, 1)
```