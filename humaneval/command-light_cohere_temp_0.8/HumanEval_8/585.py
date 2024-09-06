```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list """
    if not numbers:
        return (0, 1) 
    return (sum(numbers), product(numbers))
# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
``` 
This code provides a function `sum_product` that calculates the sum and product of a given list of integers. It handles the using empty lists and returns appropriate values.