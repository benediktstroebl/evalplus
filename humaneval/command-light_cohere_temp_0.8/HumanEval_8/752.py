```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return the sum and product of a list of integers.
    """
    list sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

#unit tests
test_sum_product = []
test_sum_product.push( ([], 0))
test_sum_product.push( [1, 2, 3, 4])
test_sum_product.push( [5, 6, 7, 8])
test_sum_product.push( [10, 20, 30, 40])
test_sum_product.push( [100, 200, 300, 400])
test_sum_product.push( [(), 1) )

def test_sum_product() :
    for test_case in test_sum_product:
        actual_result = sum_product(test_case)
        expected_result = Tuple(test_case)
        assert actual_result == expected_result, "Test failed: {}".format

test_sum_product()
```