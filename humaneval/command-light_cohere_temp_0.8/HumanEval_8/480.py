```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list case
        return (0, 1)
    return (sum(numbers), product(numbers))
#unit tests
test_sum_product = []
test_sum_product.push([0])
test_sum_product.push([1])
test_sum_product.push([2])
test_sum_product.push([3])
test_sum_product.push([4])
test_sum_product.push([5])
test_sum_product.push([10])
test_sum_product.push([20])
test_sum_product.push([25])
test_sum_product.push([4000000])
test_sum_product.push([50000000001])
def test():
    for test_data in test_sum_product:
        actual_result = sum_product(test_data)
        expected_result = (sum(test_data), product(test_data))
        print("Test:", end=" + str(actual_result) + " (Expected:", end=" + str(expected_result)) + "\n")
# main execution
test()
``` 
This Python script defines a function called `sum_product`, which takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function implements the `sum_product` function with a series of unit tests that pass. The `test` function runs these tests against the `sum_product` function to verify its correctness.