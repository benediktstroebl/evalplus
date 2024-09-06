```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
test_list = [1, 2, 3, 4]
result = sum_product(test_list)
print("Sum:", result)
print("Product:", result[1])

test_empty = []
result_empty = sum_product(test_empty)
print("Sum of an empty list:", result_empty)
print("Product of an empty list:", result_empty[1])

test_single = [5]
result_single = sum_product(test_single)
print("Sum:", result_single)
print("Product:", result_single[1])
```