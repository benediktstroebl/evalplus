```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be sorted in ascending order.
    >>> sum_product([4, 1, 2])
    (6, 4)
    >>> sum_product([1, 2, 3])
    (6, 6)
    >>> sum_product([5, 6, 7])
    (13, 42)
    >>> sum_product([1, 100])
    (101, 101)
    >>> sum_product([1, 200])
    (201, 200)
    """
    numbers = sorted(numbers)
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```  The provided Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function takes a sorted list of numbers as input and returns a tuple of two integers: the sum and the product of all the numbers in the list. The function performs the test by iterating through the list and applying the mathematical operations on each element in order.