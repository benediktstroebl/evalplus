```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.
    """
    # Initialize sum and product to their respective identity values (0 and 1)
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the total product by the number
        total_product *= num

    # Return the total sum and the total product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (available from Python 3.8) to make the function more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.
    """
    # Use the sum function to calculate the total sum
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the total product
    # If the list is empty, math.prod will return 1 by default
    total_product = math.prod(numbers, start=1)

    # Return the total sum and the total product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```