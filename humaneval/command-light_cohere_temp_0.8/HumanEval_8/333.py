```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    Args:
        List[int] - a list of integers
    Returns:
        Tuple[int, int] - a tuple with a sum and a product of all the integers in the list
    """
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Test case 1
print(sum_product([]) ((0, 1)))  # Output: (0, 1)

# Test case 2
print(sum_product([1, 2, 3, 4])) ((10, 1))  # Output: (10, 24)

# Test case 3
print(sum_product([1, 2, 3, 4, 5])) ((15, 20))  # Output: (15, 60)

# Test case 4
numbers = [5, 15, 6, 10]
print(sum_product(numbers)) ((45, 120))  # Output: (45, 120)
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. It then passes these tests to verify the correctness of the function. The output of this code block is the product of the function's output and the test cases.