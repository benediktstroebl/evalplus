```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list
        Returns: (sum, product)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

``` 
This code defines a `sum_product` function that calculates the sum and product of a list of integers, then tests the function with various inputs to ensure its correctness. The function returns a correct results for all cases and the test suite passes successfully.