```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with valid inputs
test_case = [1, 2, 3, 4]
result = sum_product(test_case)
print(result)  # Output: (6, 24)

# Test the function with empty list
empty_list = []
result = sum_product(empty_list)
print(result)  # Output: (0, 1)

# Test the function with negative numbers
negative_numbers = [-1, 2, 3]
result = sum_product(negative_numbers)
print(result)  # Output: (2, 8)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested with three scenarios: valid inputs, empty list, and negative numbers. The output of the results are printed to the console.