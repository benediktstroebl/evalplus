```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), prod(numbers))


def prod(numbers: List[int]) -> int:
    """Returns the product of the numbers in the list."""
    result = 1
    for number in numbers:
        result *= number
    return result

# Tests
numbers_list = [1, 2, 3, 4, 5]
assert sum_product(numbers_list) == (15, 120)

empty_list = []
assert sum_product(empty_list) == (0, 1)
``` 

In the above code, the prod function is introduced to calculate the product of a list of integers. The sum_product function now utilizes this separate prod function to return the product part of the result, while still retaining the sum calculation as well. This makes the code more modular and adheres to the DRY principle in programming, making it easier to maintain. 

The added test cases certify that the modifications in the code adequately resolve the problem for various cases, including non-empty and empty lists.  This helps ensure that the function behaves as expected according to the problem statement.