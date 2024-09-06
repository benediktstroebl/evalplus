```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of all the integers in a list.
    Args:
        numbers: list of integers
    Returns:
        tuple containing sum and product of all integers in the list.
    """
    return (sum(numbers), product(numbers))
```