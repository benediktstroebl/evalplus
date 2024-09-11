```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers.
    """
    # Initialize sum and product to 0 and 1 respectively, as per the problem requirements
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


# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 0, 1]))  # Expected output: (0, 0)
print(sum_product([5, 5, 5]))  # Expected output: (15, 125)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function iterates over each number in the list, adding it to the total sum and multiplying it with the total product. The function is then tested with some examples to demonstrate its correctness.