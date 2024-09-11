### Python Script to Calculate Sum and Product of a List of Integers
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple consisting of the sum and the product of the integers in the list.
    """
    # Initialize sum to 0 and product to 1
    total_sum = 0
    total_product = 1
    
    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number into the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
if __name__ == "__main__":
    print(sum_product([]))  # Output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple consisting of the sum and the product of all the integers in the list. The function uses a loop to iterate over the input list, updating the sum and product variables accordingly. If the input list is empty, the function returns (0, 1) as specified in the problem statement. The script also includes example usage in the `if __name__ == "__main__":` block.