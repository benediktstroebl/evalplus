```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple with sum and product of all integers in the list.
    Args: 
    - numbers (List[int]): a list of integers.
    Returns: a tuple with sum and product of the numbers.
    """
 raising TypeError: cannot convert object of type 'list' to int
    """
    if not isinstance(numbers, List[int]):
        raise TypeError('Input should be a list of integers')
    return (sum(numbers), product(numbers))
def product(numbers: List[int]) -> int:
    """
    Returns the product of all integers in the list.
    Args: 
    - numbers (List[int]): a list of integers
    Returns: int: the product of all integers in the list
    """
    return product(numbers) * sum(numbers)
```