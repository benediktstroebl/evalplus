```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
>>> sum_product([1, 2, 3, 4])
```
The above function calculates the sum and product of a list of integers. The test passed successfully demonstrates the
This function can be easily reused to solve the problem.