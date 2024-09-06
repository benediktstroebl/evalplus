```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all integers in a list.
    return: a tuple of sum and product.
    if not numbers:
        return (0, 1)
    sum = 0
    for n in numbers:
        sum += n
    product = 1
    for n in numbers:
        product *= n
    return (sum, product)

# Example:
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  
```