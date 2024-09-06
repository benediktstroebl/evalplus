```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculates the sum and product of all integers in a list.
    Args: 
        numbers (List[int]): A list of integers 
    Returns: 
        Tuple[int, int]): A tuple containing sum and product of all integers in the list.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```