```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple consisting of a sum and a product of all the integers in the list.
    Args:
        numbers: list of integers
    Returns:
        tuple: sum, product of the list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1,2,3,4]
test_sum_product = sum_product(numbers)
print(test_sum_product)

numbers = []
test_sum_product2 = sum_product(numbers)
print(test_sum_product2)
``` 
This code defines a function called sum_product, which takes a list of integers as an argument and returns a tuple containing the sum and product of the integers in the list. The function uses a product = 1 and sum = 0 as initial values, and then iterates through the list, multiplying the current product by each number and adding the sum of the numbers. The function then returns the product of all the integers in the list as a tuple.