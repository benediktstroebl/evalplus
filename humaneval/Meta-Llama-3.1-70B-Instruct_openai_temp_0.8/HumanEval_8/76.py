```python
from typing import List, Tuple
import math
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    
    # Calculate the sum of the numbers using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product of the numbers using the math.prod function (Python 3.8+)
    # If the list is empty, math.prod will raise a TypeError, so we use the ternary operator to return 1 in this case
    total_product = math.prod(numbers) if numbers else 1
    
    # Alternatively, you can use the functools.reduce function to calculate the product (works in Python 3.7 and earlier)
    # total_product = functools.reduce(operator.mul, numbers, 1)
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```