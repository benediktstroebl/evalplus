```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    numbers = [1, 2, 3, 4]
    product = 1
    for num in numbers:
        product *= num
    sum = sum(numbers)
    return (sum, product)

sum_product([1, 2, 3, 4])
sum_product([])  # -> (0, 1)
sum_product([5, 6, 7])  # -> (15, 56)
```
The function sum_product takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function first creates a product of all integers by iterating through the list, and then creates the sum by calling the sum function on the list.