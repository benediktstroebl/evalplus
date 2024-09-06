Here's a self-contained Python function that solves the problem you described: 

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Test for empty list
        return (0, 1)
    sum_ = sum(numbers)
    prod_ = 1
    for num in numbers:
        prod_ = prod * num
    return (sum_, prod_)
``` 
You can use this function by passing a list of integers as an argument, and it will return a tuple with the sum and product of the numbers in the list.