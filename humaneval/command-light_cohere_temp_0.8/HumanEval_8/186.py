```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of a list of integers.
    """
    sum = 0
    product = 1
    for n in numbers:
        sum += n
        product *= n
    return (sum, product)

# Example:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```