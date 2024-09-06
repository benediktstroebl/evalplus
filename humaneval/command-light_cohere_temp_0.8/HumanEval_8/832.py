```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product = product * num
    return (sum, product)

# Test cases
numbers = [0, 1]
result = sum_product(numbers)
print(result) # Output: (1, 1)

numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result) # Output: (10, 24)

numbers = []
numbers. result.
result = sum_product(numbers)
print(result) # Output: (0, 1)

numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(result) # Output: (16, 120)
```
This code defines the function `sum_product`, which takes a list of integers as input and returns a tuple of their sum and product. The function then uses the sum of the numbers in the list, and then uses a loop to multiply each number by the product. The output of the function for the test cases provided is also printed to the console.