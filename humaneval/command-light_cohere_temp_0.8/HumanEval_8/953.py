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
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
``` 
This code defines a function sum_product that calculates the sum and product of a list of integers. It uses the `typing` to define the function with the expected input types. The `sum_product` function takes a list of integers as input and returns a tuple of two integers - the sum and the product of the numbers in the list. The function uses a loop to calculate the product by multiplying the numbers in the list and adding them to the sum.