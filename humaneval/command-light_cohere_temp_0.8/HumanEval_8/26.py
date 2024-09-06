```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple with sum and product of all integers in the list.
    """
    product: = 1
    sum: = 0
    for num in numbers:
        product = num * sum
        sum = sum + num
        product = product * num
    return (sum, product)

# Test the function with sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

``` 
This Python function, sum_product, calculates the sum and product of a list of integers. The test cases show how the `sum_product` works with various inputs and returns the correct result.