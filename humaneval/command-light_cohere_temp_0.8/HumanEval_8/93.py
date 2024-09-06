```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    sum = 0
    prod = 1
    for n in numbers:
        sum += n
        prod *= n
    return (sum, prod)
```