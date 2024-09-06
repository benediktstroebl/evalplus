```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24000000
``` 
This script defines a `sum_product` function, which accepts a list of integers and returns a tuple containing their sum and product. It employs a optimized method to compute the product and sum in a single loop.