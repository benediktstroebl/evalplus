Here is a Python script that contains a self-contained function that solves the problem along with the corresponding tests:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of all integers in the list.
    >>> sum_product([]) == (0, 1)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Example usage
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It provides clear and self-contained functionality and passes the corresponding tests.