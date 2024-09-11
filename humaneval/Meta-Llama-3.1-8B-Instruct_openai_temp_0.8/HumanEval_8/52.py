Here's a Python script that solves the problem:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple where the first element is the sum of all the integers in the list and the second element is the product of all the integers in the list.
    """
    # Initialize the sum and product with the base cases
    sum_of_numbers = 0
    product_of_numbers = 1
    
    # Iterate over the list of numbers and update the sum and product
    for num in numbers:
        sum_of_numbers += num
        product_of_numbers *= num
    
    # Return the sum and product as a tuple
    return sum_of_numbers, product_of_numbers

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```
This script defines a function `sum_product` that takes a list of integers and returns a tuple of the sum and product of all the integers in the list. The function handles the base cases where the list is empty and then iterates over the list to calculate the sum and product. Finally, it returns the sum and product as a tuple. The script also includes test cases to demonstrate the function's behavior.