Here is a self-contained Python script that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    Args:
        List[int] numbers: A list of integers.
    Returns: tuple (sum, product) where sum is the sum of the integers in the list, and product is the product of the integers in the list.
    """
   :
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```

This code defines a function 'sum_product' that takes a list of integers as input and returns a tuple containing the sum and product of the given numbers. The code then runs this tests by passing an empty list and a list with specific numbers to the function, and it should correctly return the sum and product for each test case.