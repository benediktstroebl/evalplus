```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    numbers: List[int]
    sum: int
    product: int
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Testing the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```
This code defines a function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function initializes variables for the sum and product to 0 and then iterates through the input list, adding each number to the sum and multiplying it with the product to update the value.