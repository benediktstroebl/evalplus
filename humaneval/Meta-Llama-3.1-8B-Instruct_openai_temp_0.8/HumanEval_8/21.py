```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of all integers in the list.
    """
    # Check if the list is empty
    if not numbers:
        # If the list is empty, return (0, 1) as per the problem statement
        return 0, 1
    
    # Initialize sum and product variables to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the number with the total product
        total_product *= num
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines the `sum_product` function to calculate the sum and product of all integers in a given list. It handles the edge case where the list is empty, returning (0, 1) as specified in the problem statement. The script includes test cases to verify the correctness of the function.