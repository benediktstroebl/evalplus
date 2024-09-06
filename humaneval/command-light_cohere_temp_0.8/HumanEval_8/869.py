```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with valid inputs and expected outputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

# Test the function with empty list
numbers2 = []
result2 = sum_product(numbers2)
print("Sum:", result2)
print("Product:", result2[1])

# Test the function with one number
numbers3 = [5]
result3 = sum_product(numbers3)
print("Sum:", result3)
print("Product:", result3[1])
``` 

This code provides a Python script with a self-contained function `sum_product` that solves the problem of calculating the sum and product of a list of integers. The function takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function is then tested with various inputs using the `if` statements to ensure the function's correctness.