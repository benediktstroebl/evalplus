```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
print("Sum:", result)
print("Product:", result[1])
``` 
This code defines the `sum_product` function that takes a list of integers as input and returns a tuple containing their sum and product. It then passes the