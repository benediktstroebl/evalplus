Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of integers in a list:

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be non-negative integers.
    """
    The empty sum should be equal to 0 and empty product should be 1.
    """

    for i in range(len(numbers)):
        sum += numbers[i] * numbers[i]
    return (sum, sum * len(numbers))
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. It also includes type hints to indicate the expected input format.