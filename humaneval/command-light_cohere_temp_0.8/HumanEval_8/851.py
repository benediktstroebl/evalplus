```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)
# Test the function with sample input
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```