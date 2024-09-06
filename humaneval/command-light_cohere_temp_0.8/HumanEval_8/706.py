```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in the list.
    Args:
        numbers (List[int]): a list of integers
    Returns:
        Tuple[int, int]: a tuple consisting of a sum and a product of all the integers in the list
    """
    return (sum(numbers), product(numbers))

# Test the function with sample inputs
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(result)  # Output: (15, 120)
```
This code provides a function `sum_product` that calculates the sum and product of a given list of integers. The function returns a result as a tuple with the sum and product values.

The provided test case demonstrates how to use the `sum_product` function with a list of numbers and verify the correctness of the results.