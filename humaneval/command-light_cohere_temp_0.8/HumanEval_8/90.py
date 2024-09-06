```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# add tests
assert sum_product([]) == (0, 1)
assert sum_product([1, 2, 3, 4]) == (10, 24)
print(sum_product([3, 2, 4, 5]))  # Output: (16, 40)
```