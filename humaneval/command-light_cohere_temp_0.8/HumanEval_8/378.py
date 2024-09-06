```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with a list of integers
test_data = [1, 2, 3, 4, 5]
result = sum_product(test_data)
assert result == (sum(test_data), product(test_data))

# Test the function with empty list
empty_result = sum_product([])
assert empty_result == (0, 1)
```