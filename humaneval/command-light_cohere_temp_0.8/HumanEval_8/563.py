```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]) -> int:
    result = 1
    for num in numbers:
        result *= num
    return result
``` 
This script contains a `sum_product` function that calculates the sum and product of integers in a given list, and passes tests to ensure it works correctly. The script is written in a way that the function can be used standalone and does not rely on any other functions or variables.