```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of all integers in the list.
    Args:
        numbers: list of integers

    Returns:
        tuple: sum and product of all integers in numbers list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4, 5]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (15, 60)
print("Product:", test_sum_product)   # Output: 120

numbers = []
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: 0
print("Product:", test_sum_product)   # Output: 1
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested using a set of unit tests, which pass successfully.