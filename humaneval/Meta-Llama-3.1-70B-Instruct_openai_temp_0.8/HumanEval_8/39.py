```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    
    # Initialize sum to 0 and product to 1, according to the problem requirements
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the total product by the current number
        total_product *= number
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a `for` loop to iterate over the list of numbers, adding each number to the total sum and multiplying the total product by each number. The function returns a tuple containing the total sum and product.

The script also includes two test cases to verify the correctness of the function. The first test case checks that the function returns the expected result for an empty list, and the second test case checks that the function returns the expected result for a list of integers.