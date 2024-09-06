```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a given list.
    Args: numbers (List[int]): A list of integers
    Returns: tuple (int, int): A tuple containing sum and product of the integers in numbers list
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product(numbers)  # Should return (10, 24)
empty_list = []
test_sum_product(empty_list)  # Should return (0, 1)
single_num = 5
test_sum_product([single_num])  # Should return (5, 5)
```