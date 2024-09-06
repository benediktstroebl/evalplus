```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    result = numbers[0] * numbers[1]
    for num in numbers[2:]:
        result = result + num * numbers[1]
    return (result, numbers[1])

# Test the function with sample inputs
test_sum_product = sum_product([1, 2, 3, 4])
print("Test 1 Result:", test_sum_product)
print("Test 2 Result:", test_sum_product)
```