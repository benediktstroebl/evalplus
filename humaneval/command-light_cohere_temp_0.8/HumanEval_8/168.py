```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    if not numbers:  # Empty list
        return (0, 1)
    else:
        product = 1
        sum = 0
        for num in numbers:
            product *= num
            sum += num
        return (sum, product)
```  This code defines a function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the integers. It also has a test cases to ensure the function is working correctly.