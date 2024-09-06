```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list -> return 0 and 1
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
test_sum_product = [
    (5, 10),  # (sum, product)
    ([], 1),   # Empty list
    ( [1, 2, 3], 24),  # Valid list
]

results = sum_product(test_sum_product)

def assertAlmostEqual(expected, actual, places):
    assert abs((expected - actual) ** 2) < places

# Main program
assertAlmostEqual(results, test_sum_product, 1)
 ``` 
This script defines a function sum_product that calculates the sum and product of a list of integers. The test_sum_product list contains test cases, and the results are stored in the results variable. The assertAlmostEqual function is used to check if the results are close enough to the expected values.