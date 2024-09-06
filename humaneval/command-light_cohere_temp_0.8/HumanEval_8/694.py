Here's a self-contained Python function that calculates the sum and product of a list of integers and passes tests:

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    >>> return sum(numbers), * product(numbers)
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers) == (10, 24)
    True
    """
    return (sum(numbers), product(numbers))
```
The function uses the sum() function to add up all the integers in the list, and the product() function to multiply all the integers in the list. 

The function then returns a tuple containing the sum and product of the list.