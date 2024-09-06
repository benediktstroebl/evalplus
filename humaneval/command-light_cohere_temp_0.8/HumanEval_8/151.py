```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
    numbers: List[int]
    Returns:
    Tuple[sum, product]
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)

numbers = []
test_empty_list = sum_product(numbers)
print("Sum:", test_empty_list)
print("Product:", test_empty_list)

numbers = [5, 6, 7, 8]
test_double_values = sum_product(numbers)
print("Sum:", test_double_values)
print("Product:", test_double_values)
```

In this version, the function sum_product now contains the logic to calculate the sum and product of the integers in the list. The unit tests have been updated to test the function with different input scenarios, such as an empty list, a list of double numbers, and a list of integers.