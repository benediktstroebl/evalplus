```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the input list.
    """
    total_sum = sum(numbers)  # Use built-in sum function to calculate the sum of the list
    product = 1  # Initialize product to 1, as the product of an empty list is 1
    for num in numbers:
        product *= num  # Calculate the product of the list
    return total_sum, product  # Return the sum and product as a tuple


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

In this script, the `sum_product` function calculates the sum and product of a given list of integers. It uses the built-in `sum` function to calculate the sum and initializes the product to 1, as the product of an empty list is defined as 1. The function then iterates over the list, multiplying each number by the current product. Finally, it returns the sum and product as a tuple.

The script also includes two test cases to demonstrate the function's behavior. The expected output of each test case is included in the comments.