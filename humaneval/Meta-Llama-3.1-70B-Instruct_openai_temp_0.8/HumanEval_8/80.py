```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of all the integers in the list.
    """
    total_sum = sum(numbers)  # Calculate the sum of the list
    total_product = math.prod(numbers, start=1)  # Calculate the product of the list with a start value of 1
    
    return total_sum, total_product  # Return the sum and product as a tuple


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

In this script, we use the built-in Python `sum` function to calculate the sum of the list and the `math.prod` function (available in Python 3.8 and later) to calculate the product of the list. The `start` parameter of `math.prod` is set to `1` to handle the case where the input list is empty, in which case the product should be `1`. If you are using a version of Python earlier than 3.8, you can replace the `math.prod` line with the following code to achieve the same result:

```python
total_product = 1
for num in numbers:
    total_product *= num
```