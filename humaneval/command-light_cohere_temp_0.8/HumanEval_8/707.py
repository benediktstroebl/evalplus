```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    result = numbers[0] * numbers[1] + numbers[0] + numbers[1]
    for num in numbers[2:]:
        result = result * num + (result * num > 0 ? result * num : 0)
    return (result, result)

# Test cases
test_sum_product_1 = sum_product([1, 2, 3])
test_sum_product_2 = sum_product([1, 2, 3, 4])
test_sum_product_3 = sum_product([1, 2, 3, 5])
test_sum_product_4 = sum_product([10, 20, 30])

print("Test Case 1 Results:", test_sum_product_1)
print("Test Case 2 Results:", test_sum_product_2)
print("Test Case 3 Results:", test_sum_product_3)
print("Test Case 4 Results:", test_sum_product_4)
```