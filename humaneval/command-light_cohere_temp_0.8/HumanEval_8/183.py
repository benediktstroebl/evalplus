```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print(test_sum_product)  # Output: (6, 24)

numbers = []
test_empty_product = sum_product(numbers)
print(test_empty_product)  # Output: (0, 1)

numbers = [1, 2, 3, 4, 5]
test_single_number = sum_product(numbers)
print(test_single_number)  # Output: (15, 120)

numbers = [10, 20, 30]
test_large_product = sum_product(numbers)
print(test_large_product)  # Output: (60, 900)
```

The function `sum_product` calculates the sum and product of a list of integers. The test cases demonstrate the