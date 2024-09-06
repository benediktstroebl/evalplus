Here is a Python script that contains a self-contained function with proper docstrings and tests:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
    numbers: List[int] -- List of integers

    Returns:
    A tuple containing a sum and a product of all integers in the list.
    >>> help(sum_product([1, 2, 3, 4]))
    >2
    """
    if not numbers:
        return (0, 1)
    
    product = 1
    sum_ = 0
    for num in numbers:
        product *= num
        sum_ += num
    return (sum_, product)
```