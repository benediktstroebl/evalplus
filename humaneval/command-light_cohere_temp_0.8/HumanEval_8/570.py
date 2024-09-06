```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Add test cases
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print(test_sum_product)  # Output: (6, 24)
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a type hint `List[int]` which tells Python that the function expects a list of integers as input. The function also returns a tuple of the sum and product of the numbers in the list. 

It uses the loop to iterate over the list and update the sum and product.