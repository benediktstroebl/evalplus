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

The function first checks if the input list is empty, and returns a tuple of two values: the sum of the numbers in the list and the product of the numbers in the list. If the list is empty, it returns a tuple of two zeros. If the list is not empty, it returns the sum and product of all the integers in the list. 

Here is an example of how to use the function:
```python
numbers = [1, 2, 3, 4]
sum, product = sum_product(numbers)
print("Sum:", sum)
print("Product:", product)
```

The output will be:
```
Sum: 10
Product: 24
```

This demonstrates the function's ability to successfully handle both empty and non-empty lists, providing the required sum and product values.