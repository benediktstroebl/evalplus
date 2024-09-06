```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args:
    numbers: list of integers
    Returns:
    A tuple with two values, the sum and product of the list of integers.
    """
    empty sum should be equal to 0 and empty product should be equal to 1.
    """
    example usage:
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    print(result)  # Prints (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```