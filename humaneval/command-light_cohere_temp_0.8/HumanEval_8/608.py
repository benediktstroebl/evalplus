```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Tests
sum_product_test_list = [1, 2, 3, 4]
test_sum_product(sum_product_test_list) == (6, 12)
test_empty_list(sum_product_test_list) == (0, 1)
test_single_element(sum_product_test_list) == (6, 6)

def test_sum_product(test_numbers):
    return sum_product(test_numbers) == Tuple(map(int, test_numbers))

def test_empty_list(test_numbers):
    return test_sum_product(test_numbers) == (0, 1)

def test_single_element(test_numbers):
    return test_sum_product(test_numbers) == (6, 6)
```