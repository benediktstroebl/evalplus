```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]):
    result = 1
    for num in numbers:
        result *= num
    return result
```  This script defines two functions: sum_product which calculates the sum and product of a list of integers and products which generates the product of the list of integers.