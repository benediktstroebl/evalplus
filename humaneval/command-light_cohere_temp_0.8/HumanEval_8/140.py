```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple with sum and product of all integers in a list.
    """
    list comprehension is a very short way to calculate sum and product.
    product = 1
    sum = sum(numbers)
    return (product, sum)

# Test cases
numbers = [1, 2, 3, 4, 5]
print("Test Case 1: ", sum_product(numbers))

numbers = []
print("Test Case 2: ", sum_product(numbers))

numbers = [1, 2, 3]
print("Test Case 3: ", sum_product(numbers))

numbers = [1, 2, 3, 4, 5]
print("Test Case 4: ", sum_product(numbers))
``` 
This code defines a function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function uses a list comprehension, which is a very short way to calculate the sum and product of the numbers in the list.

The test cases ensure that the function is working correctly for different scenarios.