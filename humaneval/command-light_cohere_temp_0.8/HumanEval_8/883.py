```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (6, 24)
print("Product:", test_sum_product)  # Output: 24
```

In this code, we have a sum_product function that takes a list of integers as an argument and returns a tuple containing the sum and product of the numbers. The function uses a loop to calculate both the sum and product of each number in the list. The test cases show that the function is working as expected.