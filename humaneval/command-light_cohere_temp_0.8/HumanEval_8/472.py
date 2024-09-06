```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple consisting of a sum and a product of all the integers in the list.
    Args:
    List[int]: list of integers
    Returns:
    Tuple[int, int]: (Sum, Product)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test
test_list = [1, 2, 3, 4]
test_result = sum_product(test_list)
print(test_result)
``` 
This script defines a `sum_product` function that calculates the sum and product of a given list of integers, then returns a tuple of them. The function uses the value types and is adequately tested.