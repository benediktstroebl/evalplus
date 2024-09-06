```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)
```
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers. It then proceeds to calculate the sum and product using a loop, where it multiplies the numbers in the list to the product, and adds them to the sum.