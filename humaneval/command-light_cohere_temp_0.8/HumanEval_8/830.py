```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
>>> sum_product([]) ((0, 1))
>>> sum_product([1, 2, 3, 4]) ((10, 24))
```
This function takes a list of integers and returns a tuple of two integers: the sum of all the integers in the list and the product of all the integers in the list. The function is self-contained and uses a loop to iterate over the list of integers, adding each number to the sum and multiplying each number to the product. This function can be easily used to solve the problem and pass the tests.