```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case
test_list = [1, 2, 3, 4, 5]
result = sum_product(test_list)
print(f"Sum: {result[0]}, Product: {result[1]}")
``` 
This Python code defines a function called sum_product that calculates the sum and product of a list of integers. The function uses the process to calculate the sum and product, multiplying each number by the product to obtain the sum, then adding the numbers to calculate the product.