Here's the Python script with the self-contained function `sum_product` that calculates the sum and product of a given list of integers:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a given list of integers.
    Args: 
        numbers: A list of integers

    Returns: 
        A tuple consisting of a sum and a product of all the integers in the list.
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```

This function takes a list of integers as input and returns a tuple containing the sum and product of the integers. The sum is calculated by summing the integers, and the product is calculated by multiplying each integer in the list. 

This function is self-contained, and it can be used to solve the problem without relying on external code or functions.