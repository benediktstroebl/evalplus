```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    return (sum(numbers), product(numbers))
    """
    return (sum(numbers), product(numbers))

# Test case 1
test_sum_product_1 = [1, 2, 3]
test_sum_product_1_result = sum_product(test_sum_product_1)
print("Test 1 Result:", test_sum_product_1_result)

# Test case 2
test_sum_product_2 = []
test_sum_product_2_result = sum_product(test_sum_product_2)
print("Test 2 Result:", test_sum_product_2_result)

# Test case 3
test_sum_product_3 = [1, 2, 3]
test_sum_product_3_result = sum_product(test_sum_product_3)
print("Test 3 Result:", test_sum_product_3_result)
```