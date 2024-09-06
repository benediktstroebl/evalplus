```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Args:
    numbers: list[int]
        A list of integers
    Returns:
    tuple[int, int]
        A tuple containing a sum and a product of the list of integers
    """
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)
# Unit tests
test_sum_product_unit = [
    [
        None, None,
    ]
    , [1, 2, 3, 4],
    ]
test_sum_product_result = sum_product(test_sum_product_unit)
print(test_sum_product_unit == test_sum_product_result) # True
 ```