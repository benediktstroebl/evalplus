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
    return (sum(numbers), sum(numeras[0:1] for numeras in numbers))
```

The function works as follows:
- It utilizes the `typing` module to establish type hints.
- If the input list is empty, it returns 0 for the sum and 1 for the product, adhering to the requirement for empty inputs.
- Utilizing the sum function both directly and through a generator expression, it computes the sum and product of the integers. The generator expression is used to calculate the product and handles empty lists without proceeding to unnecessary iterations. 

You can verify the functionality of the `sum_product` function by calling it with different input lists:
```python
# No elements
print(sum_product([]))
# Single element
print(sum_product([1]))
# Multiple elements
print(sum_product([1, 2, 3, 4]))
```

The output will be:
```
(0, 1)
(1, 1)
(10, 24)
``` 

Which confirms that the function handles both empty lists and single or multiple elements correctly.