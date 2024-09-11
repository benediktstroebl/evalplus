### Sum and Product of a List of Integers
#### Problem Statement
Given a list of integers, return a tuple consisting of the sum and product of all the integers in the list.

#### Solution
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
    # Handle the edge case where the list is empty
    if not numbers:
        return 0, 1
    
    # Calculate the sum of the list using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product of the list using the math.prod function and a generator expression
    import math
    total_product = math.prod(numbers)
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test cases
if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
```
This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the integers. It handles the edge case where the input list is empty and uses the built-in `sum` and `math.prod` functions to calculate the sum and product, respectively. The test cases are included in the `if __name__ == "__main__":` block to ensure they are run when the script is executed directly.