Here is a self-contained Python script with a function that solves the problem of calculating the sum and product of integers in a list:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:
        return 0, 1
    """
    return_sum, product = 0, 1
    for num in numbers:
        return_sum += num
        product *= num
    return return_sum, product

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result)
```
This script defines a function sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. It also has a test cases to ensure the function is working correctly.