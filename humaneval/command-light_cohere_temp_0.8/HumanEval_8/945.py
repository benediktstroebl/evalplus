```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Unit tests
test_sum_product = [
    'def test_sum_product():
        result = sum_product([1, 2, 3])
        assert result == (3, 3)
    ]
``` 
This script defines a function 'sum_product' which takes a list of integers as input and returns a tuple of their sum and product. It also has a test case, which passes the test using the 'assert' assertion.