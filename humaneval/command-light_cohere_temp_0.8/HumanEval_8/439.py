```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

#unit tests
test_sum_product = [
    [()]
    [ [1, 2, 3], (10, 24)
    [1, 2, 3, 4], (40, 1600)
]

def test_function(func, test_data):
    actual_result = func(test_data)
    for t, (expect_sum, expect_product) in test_sum_product:
        assert actual_result == t, f"test {test_data} failed at {t}, expected {expect_sum, expect_product}"

test_function(sum_product, test_sum_product)
 ```