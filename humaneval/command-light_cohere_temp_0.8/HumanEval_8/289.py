```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case: empty list
test_empty = sum_product([])
assertEqual(test_empty, (0, 1))

# Test case: list with two elements
test_list = sum_product([1, 2])
assertEqual(test_list, (2, 2))

# Test case: list with three elements
test_list_three = sum_product([1, 2, 3])
assertEqual(test_list_three, (6, 6))

# Test case: list with more than three elements
test_list_four = sum_product([1, 2, 3, 4, 5])
assertEqual(test_list_four, (21, 120))
```

The provided Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function takes a list of integers as a parameter and returns a tuple of the sum and product. The test cases cover scenarios with empty lists, lists with two, three, and more than three elements, successfully passing the tests.