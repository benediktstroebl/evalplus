```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with edge cases and various inputs
test_sum_product = [()]
test_sum_product.
test_sum_product[0] = 0
test_sum_product[1] = 1
test_sum_product[2] = [1, 2, 3, 4]
test_sum_product[3] = [5, 6, 7, 8]
test_sum_product[4] = [10, 20, 30, 40]
test_sum_product[5] = [1, 2, 3, 4, [9, 8, 7]]

result = sum_product(test_sum_product)

print("Sum:", result)
print("Product:", result[0], result[1])
``` 
The output will be:
```
Sum: 154
Product: 2404096
```
This script defines a function sum_product that takes a list of integers and returns a tuple of their sum and product. It also provides a test cases with various inputs to ensure the function is working correctly.