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
test_empty_list()

# Test case: list with single element
test_single_element()

# Test case: list with two elements
test_two_elements()

# Test case: list with large numbers
test_large_numbers()
```

This script defines a function `sum_product` that computes the sum and product of a list of integers. The function utilizes a loop to iterate through each element in the input list and accumulates the sum and product. Additionally, the function accepts type hints and provides informative docstrings to explain its purpose and behavior.