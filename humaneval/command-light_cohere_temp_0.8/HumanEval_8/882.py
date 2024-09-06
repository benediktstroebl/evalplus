Here's a self-contained Python function that solves the problem you described: 

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list case
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)
```

This function performs the sum and product operation on a list of integers and returns the result as a tuple. 

You can use this function to solve the problem and pass tests easily.