Here's the provided code:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple with sum and product of the numbers in a list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers) 
    (6, 12)
    >>> numbers = []
    >>> sum_product(numbers) 
    (0, 1)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```

This function takes a list of integers and returns a tuple with the sum and product of the numbers in the list. It iterates through through a loop, multiplying each number to the product and adding them to the sum. Additionally, it ensures the product is initialized to 1, as the product of an empty list is 1.