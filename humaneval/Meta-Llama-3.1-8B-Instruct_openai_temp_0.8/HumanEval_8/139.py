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
    
    # Initialize sum and product to 0 and 1 respectively. 
    # These values are chosen because the sum of an empty list is 0 and the product of an empty list is 1.
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list.
    for num in numbers:
        # Add the current number to the total sum.
        total_sum += num
        # Multiply the current number with the total product.
        total_product *= num
    
    # Return a tuple containing the total sum and the total product.
    return total_sum, total_product

# Test cases
print(sum_product([]))     # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))    # Expected output: (10, 24)
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. It initializes the sum and product to 0 and 1, then iterates over each number in the list, adding it to the sum and multiplying it with the product. Finally, it returns a tuple containing the total sum and the total product. The test cases demonstrate the function's behavior for an empty list and a list with several elements.