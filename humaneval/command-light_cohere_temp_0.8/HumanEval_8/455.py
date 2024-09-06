```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.push( [None])
test_sum_product.push([0])
test_sum_product.push([1])
test_sum_product.push([2])
test_sum_product.push([3])
test_sum_product.push([4])
test_sum_product.push([5])
test_sum_product.push([10])
test_sum_product.push([-5])
test_sum_product.push([-20])

def test_sum_product() -> 
    result = sum_product(test_sum_product[0])
    assert result == (0, 1)
    for num in test_sum_product[1:-1]:
        result = sum_product(test_sum_product[0:num])
        assert result == (sum(num) , product(num)))
    result = sum_product(test_sum_product[-1: test_sum_product[-2])
    assert result == (10, 24)
``` 
The provided code defines a function `sum_product` that calculates the sum and product of a list of integers. It is tested by passing a series of unit tests, which validate the correctness of the function's output for various input scenarios.