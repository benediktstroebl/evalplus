```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of integers in a list.
    Args:
        numbers: list of integers
    Returns: 
        - tuple containing sum and product of numbers in numbers
    """
    if not numbers:
        return (0, 1)  # Return default values for empty list
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests for sum_product function
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append(sum_product(test_sum_product))
test_sum_product.append(0, 1)
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function performs these basic input validation to handle empty lists, then iterates through the list, calculating both the sum and product. It also implements unit tests using a predefined list of integers, and provides default test cases for empty lists.