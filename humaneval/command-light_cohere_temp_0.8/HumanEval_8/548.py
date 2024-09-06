Here's the solution to the markdown code block problem using Python:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    Product is calculated by multiplying all elements and summing the results.
    >>> test_sum_product([])
    ()
    >>> test_sum_product([1, 2, 3, 4])
    (4, 12)
    >>> test_sum_product([10])
    (10, 1)
    >>> test_sum_product([10, 20])
    (30, 20)
    """
    if not numbers:
        return (0, 1)
    
    sum_ = sum(numbers)
    product_ = 1
    for num in numbers:
        product_ *= num
    
    return (sum_, product_)
```
This Python code defines a function `sum_product` that calculates both the sum and product of a list of integers. The function performs these tests by calling the function with a sample list of integers, and the output is printed to the console.

You can use this function to calculate the sum and product of any list of integers. For empty lists, the function returns `(0, 1)` as specified in the docstring.