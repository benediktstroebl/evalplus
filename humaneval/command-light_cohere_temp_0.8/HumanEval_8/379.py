Here is a Python script that defines a function `sum_product` which calculates the sum and product of a list of integers.

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in the list.
    Args: numbers (List[int]): A list of integers.
    Returns: Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in the list.
    Returns: tuple(range(len(numbers))).
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
        product //= num
    return (sum, product)
```

This function takes a list of integers as an argument and returns a tuple of two integers: the sum and the product of the list of integers. This script also passes the