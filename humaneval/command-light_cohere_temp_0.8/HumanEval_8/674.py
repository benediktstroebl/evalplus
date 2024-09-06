```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    return an error if input is empty or the list is empty."""
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Example test cases
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append(5, 6, 8)
test_sum_product.append(10, 20)
test_sum_product.append([])
test_product = [1, 2, 3, 4, 5, 6, 7]
test_product = [10, 20, 40, 60]
for test_case in test_sum_product:
    actual_sum, actual_product = sum_product(test_case)
    assert actual_sum == test_case[0], f"Sum did not match. Assert: expected {test_case[0]} got {actual_sum}"
    assert actual_product == test_case[1], f"Product did not match. Assert.expect {test expected_ other expected {test_product[1]} got {actual_product}"
```