### Sum and Product of a List
#### Problem Solution

Here's a Python script that solves the problem:

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum and product with 0 and 1 respectively, as per the problem statement
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

# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function uses a simple iterative approach to calculate the sum and product. It initializes the sum and product with 0 and 1 respectively, as per the problem statement, and then iterates over each number in the list to update the sum and product. Finally, it returns the sum and product as a tuple. The script includes test cases to verify the correctness of the function.