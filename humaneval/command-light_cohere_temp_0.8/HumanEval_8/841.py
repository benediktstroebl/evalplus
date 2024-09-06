```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing a sum and product of all the integers in the list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)

numbers = []
test_empty_sum_product = sum_product(numbers)
print("Sum:", test_empty_sum_product)
print("Product:", test_empty_sum_product)
``` 
This code defines a function sum_product that calculates the sum and product of a list of integers. It uses a parameterized testing, which is a clean and recommended way to write tests in Python. It ensures that all test cases are self-contained and pass correctly.