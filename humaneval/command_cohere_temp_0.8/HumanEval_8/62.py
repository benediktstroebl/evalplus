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
```

The `prod` helper function is introduced to ensure that the product operation is performed iteratively. This approach is not only more efficient for larger lists but also aligns with the spirit of the iterative solution requested. 

The main function `sum_product` first checks if the input list is empty. If so, it promptly returns a tuple of (0, 1) according to the problem specification for an empty list. Next, it invokes `prod` to calculate the product of the list of integers, and then uses Python's built-in sum function to calculate the sum. 

This solution allows for more efficient and readable code while maintaining a self-contained function. 
To see this code in action, copy and paste it into a Python environment of your choice and run the tests:
```python
# Tests
assert sum_product([1, 2, 3, 4]) == (10, 24)
assert sum_product([]) == (0, 1)
```

Ensure that the `prod` function is used in the specifiers to demonstrate that this function is indeed integral to the solution.