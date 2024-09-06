```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function with various inputs
test_list = [1, 2, 3, 4, 5]
result = sum_product(test_list)
print(f"Sum: {result[0]} and Product: {result[1]}")
```