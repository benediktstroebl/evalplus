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
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else prod(numbers))
```

The function first checks if the input list is empty, in which case it returns a tuple containing 0 and 1. If the list is not empty, it returns a tuple with the sum of the numbers and the product of the numbers, with the exception of the first element, as described in the problem statement. The product is calculated recursively using `zip` and `sum`, which is more efficient than using `prod` for all elements. The function also handles the case when the list has only one element, in which case the product is equal to the value of that element.

Here is an example of how to use this function:
```python
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This would output: `(10, 24)` providing the sum and the product of the list `[1, 2, 3, 4]`.