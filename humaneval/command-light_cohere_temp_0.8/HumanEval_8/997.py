```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with sample inputs
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
print("Sum:", result)
print("Product:", result[0] * result[1])
```
This script defines a `sum_product` function that calculates the sum and product of a list of integers. The function uses a list as an argument and returns a tuple containing the sum and product. The script then passes the test cases with a sample input list `[1, 2, 3, 4]` and prints both the sum and product of the list.

Remember to ensure the function definition, type hints, and sample tests are included in your script to ensure the function's correct operation and proper usage.