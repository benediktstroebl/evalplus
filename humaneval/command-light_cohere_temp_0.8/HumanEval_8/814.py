```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list"""
    if not numbers:  # emptiness check
        return (0, 1)

    product = 1
    sum_ = 0
    for num in numbers:
        product *= num
        sum_ += num
    return (sum_, product)

# example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # prints (10, 24)
``` 
This code provides a self-contained function `sum_product` that calculates the sum and product of a list of integers. It uses a thorough type annotations to provide a clear and readable definition of the function, as well as input parameter types and return values. The function includes an condition for an empty list, which returns (0, 1) as the product and sum of the empty list.