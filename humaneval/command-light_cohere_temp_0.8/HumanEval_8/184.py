```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Other tests
sum_product([]) == (0, 1)
sum_product([1, 2, 3, 4]) == (10, 24)
sum_product([10, 20, 30]) == (60, 120)
sum_product([1, 2, 3]) // (2, 6) == 5
```