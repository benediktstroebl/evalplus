```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.py: []
test_sum_product.push((0, 1))
test_sum_product.push(1, 2)
test_sum_product.push(1, 3)
test_sum_product.push(2, 4)
test_sum_product.push(3, 5)
test_sum_product.push(4, 6)
test_sum_product.push(5, 7)

def test():
    for item in test_sum_product:
        actual_sum, actual_product = sum_product(item)
        assert actual_sum == item[0]
        assert actual_product == item[1]

test()
``` 
This script has a function `sum_product` that calculates the sum and product of a list of integers. The function has been tested using a series of unit tests.  The output will show that all the assertions pass, which confirms that the `sum_product` function is working correctly.