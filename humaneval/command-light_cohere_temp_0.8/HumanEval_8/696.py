```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    Args:
    numbers: list of integers
    Returns:
    tuple: (Sum of integers, Product of integers)
    """
    if not numbers:  # empty list
        return (0, 1)
    sum_ = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum_, product)
test_data = [1, 2, 3, 4]
test_output = sum_product(test_data)
print(test_output) # prints (10, 24)
```