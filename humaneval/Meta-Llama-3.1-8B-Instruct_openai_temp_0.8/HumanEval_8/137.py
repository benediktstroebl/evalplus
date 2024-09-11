```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple of sum and product of all the integers in the list.
    """
    
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        
        # Multiply the number with the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

In this script, we define a function `sum_product` that takes a list of integers as input and returns a tuple of the sum and product of all the integers in the list. We use a simple loop to iterate over each number in the list, adding it to the total sum and multiplying it with the total product. The function returns the total sum and product as a tuple. The script also includes two test cases to verify the correctness of the function.