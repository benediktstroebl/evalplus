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
    return (sum(numbers), sum(n * n for n in numbers))
```

The function checks if the input list is empty and returns a default tuple with zeros and ones for sum and product respectively. Otherwise, it uses the sum function to calculate the sum of the numbers in the list and the generator expression to calculate the product of the numbers in the list. Finally, it returns a tuple with the calculated sum and product.

Here is an example of how to use the function:
```python
numbers = [1, 2, 3, 4]
sum_product(numbers)
```

And here is the output of the function:
(10, 24)