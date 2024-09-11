```python
from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.
    """
    # Calculate the sum of the numbers using the built-in sum function.
    # If the list is empty, sum returns 0, which is the desired behavior.
    total_sum = sum(numbers)
    
    # Calculate the product of the numbers using the reduce function from the functools module.
    # The reduce function applies a binary function (in this case, the multiplication operator) to all items in an iterable, going from left to right, so as to reduce the iterable to a single output.
    # If the list is empty, reduce returns 1, which is the desired behavior, but only if we provide 1 as the initializer.
    # We use the operator.mul function as the binary function, which is the function that corresponds to the multiplication operator (*).
    total_product = reduce(operator.mul, numbers, 1)
    
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```