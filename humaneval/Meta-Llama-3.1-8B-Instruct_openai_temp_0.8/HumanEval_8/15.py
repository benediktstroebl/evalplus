### Sum and Product of Integers in a List
#### Python Script
```markdown
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """

    # Initialize sum and product with 0 and 1 respectively
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


# Example usage:
if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
    print(sum_product([-1, 2, -3, 4]))  # (-0, -24)
```

### Explanation
This script defines a function called `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. If the list is empty, it returns a tuple with 0 as the sum and 1 as the product. The script also includes example usage and docstrings for better understanding.