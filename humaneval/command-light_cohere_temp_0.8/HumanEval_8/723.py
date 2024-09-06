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
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
print("Sum:", result)
print("Product:", result[1])
```