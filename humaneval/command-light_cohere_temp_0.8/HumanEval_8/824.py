Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    >>> numbers = [1, 2, 3, 4]
    total, product = sum_product(numbers)
    print("Sum:", total)
    print("Product:", product)
    """
    total = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total, product
```

This code defines a function called `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function uses the use of the built-in function `sum` and iterates through the list using a loop to calculate the sum and product.

This code follows the functional programming paradigm, which promotes reusability and modularity in the code. It also uses type annotations to provide better type hints and documentation.