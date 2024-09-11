```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple where the first element is the sum of the list and the second element is the product of the list.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize variables to keep track of sum and product using list methods
    num_sum = sum(numbers)
    num_product = 1
    # If the list is not empty, calculate the product using the reduce function
    if numbers:
        num_product = 1
        for num in numbers:
            num_product *= num

    return num_sum, num_product

# Test cases
print(sum_product([]))  # Expected (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected (10, 24)
```

In this code, we have a function `sum_product` that calculates the sum and product of a list of numbers. It uses the built-in `sum` function to calculate the sum and a simple loop to calculate the product. 

For the product calculation, we've used a loop as Python's built-in `math.prod` function is available only in Python 3.8 and later. 

This script includes docstrings for the function to provide information about the function's purpose, parameters, return values, and examples of usage. The test cases at the end of the script demonstrate how to use the function with different inputs.