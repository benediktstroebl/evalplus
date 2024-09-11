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
    sum_of_numbers = 0  # Initialize sum to 0
    product_of_numbers = 1  # Initialize product to 1

    # Iterate over the input list
    for number in numbers:
        sum_of_numbers += number  # Add the current number to the sum
        product_of_numbers *= number  # Multiply the current number with the product

    return sum_of_numbers, product_of_numbers  # Return the sum and product as a tuple

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function according to the provided specification. It initializes the sum and product variables to 0 and 1, respectively. Then, it iterates over the input list, updating the sum and product as it goes. Finally, it returns the sum and product as a tuple. The script also includes test cases to demonstrate the function's behavior.