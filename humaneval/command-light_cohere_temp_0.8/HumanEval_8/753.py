```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]):
    result = 1
    for num in numbers:
        result *= num
    return result
``` 
This code defines two functions: sum_product and products. The sum_product function takes a list of integers as input and returns a tuple of the sum of the list and the product of the list. The products function takes a list of integers and returns the product of the list.