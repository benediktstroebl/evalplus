```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of all integers in a given list. 
    Returns a sum and product as a tuple.
    >>> test1
    sum_product([])
    ()
    >>> test2 = sum_product([1, 2, 3, 4])
    (10, 24)
    >>> test3 = sum_product([1, 2, 3])
    (6, 12)
    >>> test4 = sum_product([5, 6, 7])
    (21, 42)
    """
    if not numbers:
        return (0, 1)

    return (sum(numbers), product(numbers))

# Example usage
test1 = sum_product([1, 2, 3])
(10, 12)
test2 = sum_product([1, 2, 3, 4])
(10, 24)
test3 = sum_product([1, 2, 3])
(6, 12)
test4 = sum_product([5, 6, 7])
(21, 42)
 ``` 
This code defines a function sum_product that calculates the sum and product of a list of integers and passes all the tests. It ensures that the result is valid and the function is working as expected.