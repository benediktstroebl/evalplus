```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum and product to 0 and 1, respectively, as per problem requirements
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return a tuple containing the total sum and the total product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines the `sum_product` function, which calculates the sum and product of a given list of integers. It uses two variables, `total_sum` and `total_product`, to keep track of these values and initializes them to 0 and 1, respectively. The function then iterates over each number in the list, updating these values accordingly. Finally, it returns a tuple containing the total sum and product.