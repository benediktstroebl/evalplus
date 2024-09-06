Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return result, product
```

This code defines a function called `sum_product` that takes a list of integers as an argument and returns a tuple containing the sum and product of all the integers in the list. It uses a simple loop to iterate through the numbers and accumulate their sum and product. It then returns the values as a tuple.