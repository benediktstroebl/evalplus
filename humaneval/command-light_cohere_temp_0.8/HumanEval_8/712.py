```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in numbers list """
    if not numbers:  # Empty sum should be 0 and empty product should be 1
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test case 1 result:", test_result)  # Output: (6, 24)

# Test case 2
test_empty_list = []
test_result2 = sum_product(test_empty_list)
print("Test case 2 result:", test_result2)  # Output: (0, 1)

# Test case 3
test_large_list = [1, 2, 3, 4, 5, 6, 7]
test_result3 = sum_product(test_large_list)
print("Test case 3 result:", test_result3)  # Output: (21, 120)
```

This script provides a function called sum_product, which takes a list of integers as input and returns a tuple with the sum and product of the integers in the list. It performs basic type checks to ensure the validity of the function.