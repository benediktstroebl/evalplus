```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)  # Calculate the sum of the numbers in the list
    total_product = 1  # Initialize the product to 1
    
    # If the list is not empty, calculate the product
    if numbers:
        total_product = 1  # Initialize the product to 1
        for num in numbers:
            total_product *= num  # Multiply the product by each number in the list
    
    # Alternatively, you can use the math.prod function (Python 3.8+) to calculate the product
    # import math
    # total_product = math.prod(numbers) if numbers else 1
    
    return total_sum, total_product  # Return the sum and product as a tuple


# Example use cases:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses the built-in `sum` function to calculate the sum and a for loop to calculate the product. If the list is empty, it returns a sum of 0 and a product of 1, as specified in the problem statement. The script also includes example use cases to demonstrate the function's usage.