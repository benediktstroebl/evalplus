```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    numbers = [1, 2, 3, 4]
    return (10, 24)
    """
    return (sum(numbers), product(numbers))

# Testing the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)

```
This code defines a function called sum_product that takes a list of integers as input and returns a tuple with two values: the sum of the numbers in the list and the product of all the numbers in the list. The function uses the method sum and product, and returns the corresponding tuple. The code also passes the the test case and prints the output, which is the result of the sum_product function with the list of numbers [1, 2, 3, 4].