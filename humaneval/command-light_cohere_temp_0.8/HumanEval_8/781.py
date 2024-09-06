```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Testing the function
test_numbers = [1, 2, 3, 4, 5]
result = sum_product(test_numbers)
assert isinstance(result, Tuple), "Function returned unexpected type."
assert len(result) == 2, "Function did not return tuple with expected length."
assert result[0] == 5  , "Sum is not 5"
assert result[1] == 120, "Product is not 120"

```