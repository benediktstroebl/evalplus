```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit Tests
test_sum_product = [
    [
        ((), (0, 1)),
        ([], (0, 1)),
        ([1, 2, 3, 4], (6, 12))
    ]
def test_sum_product_func():
    for test_case in test_sum_product:
        actual_result = sum_product(test_case)
        expected_result = test_case
        assert actual_result == expected_result, f"Test case [{test_case}] failed."
test_sum_product_func()
```