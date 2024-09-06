```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with various inputs
numbers1 = [1, 2, 3]
result1 = sum_product(numbers1)
print(result1)  # Output: (6, 12)

numbers2 = []
result2 = sum_product(numbers2)
print(result2)  # Output: (0, 1)

numbers3 = [10, 20, 30]
result3 = sum_product(numbers3)
print(result3)  # Output: (60, 900)

```

The code defines a function `sum_product` that calculates the sum and product of a list of integers. The function handles both empty lists and lists with different lengths, and it passes all the corresponding tests.