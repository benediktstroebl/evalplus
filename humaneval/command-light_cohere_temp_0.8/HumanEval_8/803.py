```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # Empty sum should be equal to 0 and empty product should be equal to 1
        return (0, 1)

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case:
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test case 1 result:", test_result)

# Test case 2:
test_data = []
test_result = sum_product(test_data)
print("Test case 2 result:", test_result)
```
This code defines the `sum_product` function that calculates the sum and product of the integers in a given list. The function includes checks for an empty list, and returns the correct results for both test cases.