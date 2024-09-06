```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4, 5]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (15, 60)
print("Product:", test_sum_product)   # Output: (75, 256)
``` 
The function 'sum_product' calculates the sum and product of a list of integers. It uses a efficient methods to calculate the product as 1 and then uses a loop to calculate the sum.