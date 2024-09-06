```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    :return [sum(numbers), (sum(numbers)) * prod(numbers)]
    """
    return (sum(numbers), (sum(numbers)) * prod(numbers))

# This function uses built-in Python functions, specifically sum and prod from math module

# Test cases
numbers = [1, 2, 3, 4]
print(sum_product(numbers)) == (sum(numbers), 1224)
```