```markdown
### Python Script to Calculate Sum and Product of a List of Integers

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of the sum and product of the input list.
    """
    # Initialize sum and product with 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number to the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

### Explanation:

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. If the input list is empty, the function returns `(0, 1)` as per the problem requirements. The function uses a simple iteration approach to calculate the sum and product of the input list. The test cases at the end demonstrate the function's usage with an empty list and a list with some integers.