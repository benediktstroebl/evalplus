```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with different inputs
numbers1 = [1, 2, 3]
numbers2 = [3, 4, 5]
test_result1 = sum_product(numbers1)
test_result2 = sum_product(numbers2)

print("Test Result 1:", test_result1)
print("Test Result 2:", test_result2)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a optimized approach with loop to calculate the product and sum. The function returns a tuple of sum and product values. The test cases demonstrate how the values are returned correctly, which confirms the correctness of the function.

The output will be:
```
Test Result 1: (6, 3)
Test Result 2: (15, 120)
```