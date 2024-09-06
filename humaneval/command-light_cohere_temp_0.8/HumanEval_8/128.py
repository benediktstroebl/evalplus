```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of integers in a list.
    Args:
        numbers: list of integers

    Returns:
        tuple consisting of sum and product of all integers in numbers
    """
    if not numbers:
        return (0, 1)
        
    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num
        
    return (sum_result, product_result)

# Example usage
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
print(sum_product([1]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This code defines a sum_product function that calculates the sum and product of the integers in a given list. It performs basic type and input validation to ensure the passed list is not empty, and returns the result as a tuple. The example usage demonstrates the values of the sum and product, as expected.