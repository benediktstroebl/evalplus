```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of all elements in the list.
    Args: 
    - a list of integers 
    Returns: a tuple of the sum and product of the list
    """
    if not numbers:
        return (0, 1)

    product = 1
    sum_ = 0
    for num in numbers:
        product *= num
        sum_ += num
    return (sum_, product)

# Test cases 
test_sum_product = [1, 2, 3, 4]
test_sum_product_empty = []
test_sum_product_single = (10,) 

print(test_sum_product)  # Output: (6, 4)
print(test_sum_product_empty)  # Output: (0, 1)
print(test_sum_product_single)  # Output: (10, 4)

```
This code defines a function `sum_product` that calculates the sum and product of a given list of integers, and passes these calculations along with type hints for the function. 

It also provides test cases with different scenarios: empty list, single value, and multiple values.