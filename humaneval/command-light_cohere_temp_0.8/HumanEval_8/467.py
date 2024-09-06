```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]} , Product: {result[1]}")  # prints (10, 24)
``` 
This Python code defines a function called sum_product, designed to compute the sum and product of a list of integers. The function takes a input as a list of integers, and returns a tuple containing the sum and product of the numbers. In the test, the function is applied to the list [1, 2, 3, 4], and the result is printed to the console, showing the sum (10) and product (24) as expected.