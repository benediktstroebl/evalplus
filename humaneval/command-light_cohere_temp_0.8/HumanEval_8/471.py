```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Args:
    numbers: list of integers
    Returns:
    tuple[int, int]: (sum of the numbers, product of the numbers) 
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This code provides a self-contained solution to the problem described, which is to calculate the sum and product of a given list of integers and return them in a tuple.

The sum_product function takes a list of integers as input and returns a tuple of two integers - the sum of the numbers and the product of the numbers. The output of the sum and product are then printed to the console.