Here's the self-contained Python function that solves the problem of calculating the sum and product of integers in a list:

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    if not numbers:
        return 0, 1
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return sum, product
```

This function takes a list of integers as input and returns a tuple with two values: the sum of the list and the product of the list's elements. The function also includes a condition to handle an empty list, returning 0 and 1.

The sum of the list is calculated using the sum() function, and the product of the list's elements is calculated using a loop that multiplies each element to the product variable.