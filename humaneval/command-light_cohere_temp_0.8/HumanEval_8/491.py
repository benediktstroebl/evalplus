```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Returns a tuple with sum and product of integers in a list.
    Numbers should be positive integers. Returns an tuple with 0 as sum and 1 as product 
    product for an empty list.
    """

    list may contain at least one integer
    """
    if not numbers:  # Empty list
        return (0, 1)
    sum = numbers[0]
    for num in numbers[1:]:
        sum += num
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)
```