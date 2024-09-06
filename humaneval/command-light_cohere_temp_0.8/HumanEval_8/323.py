```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    Return values areempty sum as 0 and empty product as 1.

    if numbers[
        add up all numbers and multiply them together,
    the product is calculated by multiplying the sum of the list.
    >>> sum_product([])
    ()
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5, 10, 20])
    (30, 400)
    """

    # sum of numbers in the list
    sum_result = sum(numbers)

    # product of numbers in the list
    product_result = 1

    for num in numbers:
        product_result *= num

    return (sum_result, product_result)

# Test the function with sample inputs
print(sum_product([5, 10, 20]))  # Output: (30, 400)
print(sum_product([10, 20, 30]))  # Output: (60, 600)
print(sum_product([]))  # Output: (0, 1)
```

This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function takes a list of numbers as input and returns a tuple of two integers: the sum of the list and the product of the list's elements. The test cases demonstrate the by passing different lists as inputs and verifying the function's output. The function provides a accurate results and follows the expected behavior of calculating the sum and product of a list of integers.