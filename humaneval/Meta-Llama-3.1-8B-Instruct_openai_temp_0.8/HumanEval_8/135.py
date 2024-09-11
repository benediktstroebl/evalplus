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
    
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
if __name__ == "__main__":
    # Test case 1: Empty list
    print(sum_product([]))  # Expected output: (0, 1)
    
    # Test case 2: List with integers
    print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of a given list of integers. The function initializes `total_sum` to 0 and `total_product` to 1, then iterates over the list, adding each number to `total_sum` and multiplying `total_product` by the number. Finally, the function returns a tuple containing the sum and product. The script includes test cases to demonstrate the function's behavior with an empty list and a list with integers.