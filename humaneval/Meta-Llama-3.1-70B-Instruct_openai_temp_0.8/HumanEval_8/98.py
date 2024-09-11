```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of all integers in the list.
    """
    # Initialize sum to 0 (neutral element for addition) and product to 1 (neutral element for multiplication)
    sum_result = 0
    product_result = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the sum
        sum_result += number
        # Multiply the number with the current product
        product_result *= number
    
    # Return the calculated sum and product as a tuple
    return sum_result, product_result


# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

You can also use built-in functions `sum` and `math.prod` to simplify the code:

```python
import math
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of all integers in the list.
    """
    # Calculate sum using built-in sum function
    sum_result = sum(numbers)
    
    # Calculate product using math.prod function (Python 3.8+)
    product_result = math.prod(numbers, start=1)
    
    # Return the calculated sum and product as a tuple
    return sum_result, product_result


# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```