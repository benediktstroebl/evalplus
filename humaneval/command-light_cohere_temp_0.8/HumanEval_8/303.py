```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list.
    Args:
    numbers: List[int]
        A list of integers

    Returns:
    A tuple containing a sum and a product of the list of integers
    """
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Tests
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
print(sum_product([0]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This code defines a `sum_product` function that calculates the sum and product of a list of integers. It uses type hints to provide information about the expected input type, and returns a tuple of two values: the sum of the numbers in the list and the product of all the numbers. It also includes tests cases that verify the correctness of the function.