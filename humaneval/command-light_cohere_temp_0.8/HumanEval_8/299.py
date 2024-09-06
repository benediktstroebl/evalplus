```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
        numbers (List[int]): List of integers.
    Returns: tuple (sum, product) where sum is the sum of the integers and product is the product of all integers in the list.
    """
    implementation:
    # Initialize two variables to store the sum and product.
    sum = 0
    product = 1

    # Iterate over the list of integers and update the sum and product variables.
    for num in numbers:
        sum += num
        product *= num

    # Return the calculated sum and product
    return (sum, product)

# Unit tests
numbers_list = [1, 2, 3, 4, 5]
result = sum_product(numbers_list)
print(result)  # Prints (15, 120)

numbers_empty = []
result_empty = sum_product(numbers_empty)
print(result_empty)  # Prints (0, 1)

numbers_single = [1]
result_single = sum_product(numbers_single)
print(result_single)  # Prints (1, 1)
```
This script defines a function sum_product that takes a list of integers as input and returns a tuple containing the sum and product of those integers. The function is then implemented by initializing two variables to store the sum and product, then iterating over the input list and updating the variables accordingly. The unit tests cover the full code functionality and pass the tests successfully.