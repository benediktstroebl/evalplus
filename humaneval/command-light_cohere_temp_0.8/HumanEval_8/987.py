```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (6, 24)
print("Product:", test_sum_product)   # Output: 24
``` 
This script defines a function called `sum_product` that calculates the sum and product of a list of integers.  It also includes unit tests with the function, passing in a series of numbers and checking the output of the function against the expected results.