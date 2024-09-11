```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the given numbers.
    """
    
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number to the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. It uses a for loop to iterate over each number in the list, adding the current number to the total sum and multiplying it to the total product. If the list is empty, it returns (0, 1) as per the problem statement. The script also includes example usage to demonstrate the function's behavior.