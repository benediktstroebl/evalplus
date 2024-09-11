**Sum Product Calculator**
==========================

Here's a Python script that implements the `sum_product` function as per the given specifications:

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum and product variables to 0 and 1 respectively
    total_sum = 0
    product = 1

    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        product *= num

    # Return the sum and product as a tuple
    return total_sum, product

# Example usage
if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines the `sum_product` function, which calculates the sum and product of a given list of integers. The function initializes the sum and product variables to 0 and 1, respectively, and then iterates over the input list, updating the sum and product variables accordingly. Finally, the function returns the sum and product as a tuple.

The script also includes an example usage section, which demonstrates how to use the `sum_product` function with an empty list and a non-empty list.