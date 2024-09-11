```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the given list of integers.
    """
    sum_of_numbers = 0
    product_of_numbers = 1
    
    # Iterate over the given list of integers
    for number in numbers:
        # Add the current integer to the sum
        sum_of_numbers += number
        # Multiply the current integer with the product
        product_of_numbers *= number
    
    # Return the sum and product as a tuple
    return sum_of_numbers, product_of_numbers

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the given list. The function handles both empty lists and lists with multiple elements, returning the expected results as per the problem statement. The script also includes example test cases to verify the correctness of the function.