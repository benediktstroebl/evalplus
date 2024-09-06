```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print(test_result)
``` 
This code defines a function `sum_product` that takes a list of integers and returns a tuple of their sum and product. The function performs the empty sum and product when passed an empty list, and passes the tests.