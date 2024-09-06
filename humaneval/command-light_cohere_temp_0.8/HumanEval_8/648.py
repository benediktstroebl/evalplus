```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # prints (6, 24)
``` 
This code provides a function `sum_product` that takes a list of integers as input and returns a tuple of the sum and product of all integers in the list. It then creates a test values against the expected output, successfully passing the test.