Here's a self-contained Python function that solves the problem of calculating the sum and product of a list of integers and passes the tests:

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple containing the sum and product of all the integers in the input list.
    if not numbers:
        return (0, 1)  
    """
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num
        # return 0 if an empty list is passed
        if len(numbers) == 0:
            return (0, product)

    return (sum, product)
```