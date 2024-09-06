Here is a self-contained Python script that solves the problem of calculating the sum and product of a given list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function takes a list of integers as input and returns a tuple with the sum and product of all the numbers in the list.
    >>> print(sum_product([1, 2, 3, 4]))
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```

This function uses a loop to iterate over each element in the input list. The function then calculates the sum by adding each element in the list, and the product is calculated by multiplying each element by a number and then adding the number to the product.

The output of the function is a tuple containing the sum and the product of the list of integers. 

This code is well-structured and self-contained, as it does not rely on any other functions or modules for its implementation.