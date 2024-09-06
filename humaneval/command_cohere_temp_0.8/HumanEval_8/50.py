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

The `prod` helper function is introduced to ensure clarity and encapsulation. The main function `sum_product` is easier to understand and more versatile with this improvement. 

Both functions are fully typed. The type hint `List[int]` indicates that the function `prod` accepts a list of integers as input and returns the product of these integers. 

This code is concise, readable, and maintains code reuse, clarity, and encapsulation. 

The Markdown code block above includes a quick test to check the main function `sum_product` performance with the list of integers `[1, 2, 3, 4]`. The expected result is `(10, 24)`. 

To better understand the `prod` helper function, let's test it separately:
```python
>>> prod([1, 2, 3, 4])
24
>>> prod([])
1
>>> prod([1, 2, 3])
6
```

The `prod` function is versatile and can be applied to the lists of different lengths and with different content. It follows the `DRY` principle and is a reusable building block for solving related problems.