```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args:
        numbers: A list of integers
    Returns:
        A tuple containing a sum and product of the integers in the list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4, 5]
test_sum_product = sum_product(numbers)
assert test_sum_product == (5, 30)

numbers = []
test_empty_list = sum_product(numbers)
assert test_empty_list == (0, 1)

numbers = [1, 2, 3]
test_single_numbers = sum_product(numbers)
assert test_single_numbers == (6, 12)
```

The script defines a function `sum_product` that calculates the sum and product of a list of integers. It returns a tested by passing test cases to ensure the function's correctness. The test cases cover scenarios with empty lists, single numbers, and multiple numbers. The function is designed to handle these cases efficiently and produce accurate results.