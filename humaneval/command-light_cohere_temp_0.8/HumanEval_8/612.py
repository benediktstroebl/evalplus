Here's a self-contained Python script that includes the function `sum_product`, along with the corresponding tests:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # empty list test
        return (0, 1) 
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case: empty list
test_sum_product([])  # => (0, 1)

# Test case: list with single element
test_sum_product([1])  # => (1, 1)

# Test case: list with two elements
test_sum_product([1, 2])  # => (2, 2)

# Test case: list with three elements
test_sum_product([1, 2, 3])  # => (6, 6)

# Test case: list with four elements
test_sum_product([1, 2, 3, 4])  # => (10, 24)
```
This code defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing their sum and product. The function performs basic validation to ensure the input is not empty and then performs the calculation using a loop. The test cases at the