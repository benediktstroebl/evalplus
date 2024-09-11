```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num
    
    # Return a tuple of the total sum and the total product
    return total_sum, total_product

# Test the function
print(sum_product([]))    # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))    # Output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a simple loop to iterate over the list, adding each number to the sum and multiplying each number with the product. The function returns a tuple containing the sum and product. The test cases at the end of the script demonstrate the function's behavior with an empty list and a list of positive integers.