```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple where the first element is the sum of all numbers in the list, and the second element is the product of all numbers in the list.
    """
    
    # Initialize sum and product to 0 and 1 respectively, as specified in the problem statement
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        
        # Multiply the current number with the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all numbers in the list. The function uses a loop to iterate over each number in the list, adding it to the sum and multiplying it with the product. The function then returns the sum and product as a tuple. The script also includes some test cases to demonstrate the function's behavior.