```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
# Example usage
numbers = [1, 2, 3, 4]
result, product = sum_product(numbers)
print("Sum:", result)
print("Product:", product)
```