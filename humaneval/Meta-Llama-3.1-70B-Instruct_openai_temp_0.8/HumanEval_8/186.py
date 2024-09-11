```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input list.
    """
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the total product by the number
        total_product *= num
    
    # Return the total sum and the total product
    return total_sum, total_product

# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

Alternatively, you can also use the built-in `sum` function and the `math.prod` function (available in Python 3.8 and later) to make the code more concise:

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
        Tuple[int, int]: A tuple containing the sum and the product of the input list.
    """
    # Return the sum and the product of the input list
    return sum(numbers), math.prod(numbers, start=1)

# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

Note that the `math.prod` function uses the `start` parameter to specify the starting value of the product, which is 1 in this case. If the input list is empty, `math.prod` will return the starting value, which is 1.