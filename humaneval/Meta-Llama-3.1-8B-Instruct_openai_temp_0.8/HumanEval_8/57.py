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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    sum_of_numbers = 0
    product_of_numbers = 1
    
    # Iterate over the numbers in the list
    for number in numbers:
        # Add the current number to the sum
        sum_of_numbers += number
        # Multiply the current number with the product
        product_of_numbers *= number
    
    # Return the sum and product as a tuple
    return sum_of_numbers, product_of_numbers

# Example usage:
print(sum_product([]))
print(sum_product([1, 2, 3, 4]))
```

This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. It initializes variables to keep track of the sum and product, then iterates over the list, updating these variables. Finally, it returns the sum and product as a tuple. The example usage demonstrates how to use this function with an empty list and a list containing some integers.