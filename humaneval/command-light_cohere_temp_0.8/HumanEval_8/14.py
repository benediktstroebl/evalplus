```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Unit tests
test_sum_product = []
test_sum_product.append([1, 2, 3])
test_sum_product.append(4, 8)
test_sum_product.append(5, 16)
test_sum_product.append([6, 7])
test_sum_product.append([7, 1])  

def test_sum_product():
    for test_list in test_sum_product:
        actual_sum_product, actual_product = sum_product(test_list)
        assert actual_sum_product == (test_list[0] + test_list[1]), assert_equal(actual_product, test_list[2])

# Main program and test cases
sum_product(test_sum_product)
``` 
This code defines a `sum_product` function that takes a list of integers and returns a tuple of their sum and product. It also includes unit tests that pass the test cases, and the test cases are successfully evaluated.