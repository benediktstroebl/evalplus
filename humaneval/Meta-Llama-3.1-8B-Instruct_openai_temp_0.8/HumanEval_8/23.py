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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Use the built-in sum function to calculate the sum of the list.
    # If the list is empty, sum will return 0.
    total_sum = sum(numbers)
    
    # Use the built-in prod function from the math module to calculate the product of the list.
    # If the list is empty, prod will return 1.
    import math
    total_product = math.prod(numbers)
    
    # Return a tuple containing the sum and product.
    return total_sum, total_product

# Test the function with examples
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

Alternatively, if you want to avoid using the built-in `prod` function, you can use a generator expression to calculate the product:

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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Use the built-in sum function to calculate the sum of the list.
    # If the list is empty, sum will return 0.
    total_sum = sum(numbers)
    
    # Use a generator expression to calculate the product of the list.
    # The expression (1 for x in numbers if numbers) ensures that the product is 1 if the list is empty.
    total_product = 1
    for num in numbers:
        total_product *= num
    
    # Return a tuple containing the sum and product.
    return total_sum, total_product

# Test the function with examples
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```