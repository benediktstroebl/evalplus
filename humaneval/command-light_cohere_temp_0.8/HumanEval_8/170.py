```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in the list.
    Args:
        numbers (List[int]): A list of integers
    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)
```