```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case: empty list
test_empty_list()
def test_empty_list():
    return sum_product([]) == (0, 1)
# Test case: list with two elements
test_list_with_two_elements()
def test_list_with_two_elements():
    return sum_product([1, 2]) == (1, 2)
# Test case: list with three elements
test_list_with_three_elements()
def test_list_with_three_elements():
    return sum_product([1, 2, 3]) == (3, 6)
# Test case: list with large elements
test_large_list()
def test_large_list():
    return sum_product([10, 100, 1000]) == (3100, 40000)
# Test case: list with negative elements
test_negative_elements()
def test_negative_elements():
    return sum_product([1, 2, -3]) == (-2, -6)
```
This Python script defines a self-contained function `sum_product` that solves the problem of calculating the sum and product of a given list of integers. The function takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The script also includes various test cases to verify the correctness of the `sum_product` function.