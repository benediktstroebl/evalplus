```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute sum and product of integers in a list.
    Args: 
        numbers: list of integers
    Returns: 
        tuple: (sum, product) where sum is the sum of the numbers and product is the product of the numbers
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit Tests
numbers_test_list = [1, 2, 3, 4, 5]
test_result = sum_product(numbers_test_list)
print(test_result)

numbers_empty_list = []
empty_test_result = sum_product(numbers_empty_list)
print(empty_test_result)

numbers_single_element = [1]
single_element_test_result = sum_product(numbers_single_element)
print(single_element_test_result)
``` 
This Python code defines a function `sum_product` that calculates both the sum and product of a list of integers. The function takes a input as a list of integers and returns a tuple containing the sum and product of the integers. Additionally, there are unit tests that verify the correctness of the `sum_product` function with different input scenarios.