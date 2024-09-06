```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = [5, 2, 3]
result = sum_product([5, 2, 3])
print("Sum:", result)
print("Product:", result[1])
``` 
This function, `sum_product`, takes a list of integers as input and returns a tuple with the sum and product of the integers. It uses a `product = 1` to initialize the product and then loops through the list, updating the product and sum.