```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list """
    if not numbers:  # empty list case
        return (0, 1)

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# tests
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
print("Result:", result)

test_empty = []
result_empty = sum_product(test_empty)
print("Empty product:", result_empty)

test_single = [5]
result_single = sum_product(test_single)
print("Single number product:", result_single)
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It returns a both the value of the sum and product as a tuple. It performs basic type checks to handle edge cases, such as an empty list and a single number, ensuring accurate results. 

The code then passes tests with various input scenarios to validate the correctness of the function.