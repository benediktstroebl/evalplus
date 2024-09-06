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
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}  / Product: {result[1]}")
```