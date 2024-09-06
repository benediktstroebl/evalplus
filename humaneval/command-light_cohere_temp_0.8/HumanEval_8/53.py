```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
>>> sum_product([1, 2, 3, 4])
(10, 24)
``` 
This code defines a function called sum_product, which takes a list of integers as an argument. It initializes two result to 0 and product to 1. Then, it iterates through the list and adds each integer to the result and multiplies it with product. This process continues until all list is empty.