```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))

# Unit tests
test_sum_product = []
test_sum_product.push( (-1, ) )
test_sum_product.push( (2, 4) )
test_sum_product.push( (5, 10) )
test_sum_product.push( (10, 100) )
test_sum_product.push( (1, 5) )
test_sum_product.push( (0, 0) )  

for test in test_sum_product:
    actual = sum_product(test)
    expected = (sum(test), product(test))
    assert actual == expected, f"Test {test} failed" 
```