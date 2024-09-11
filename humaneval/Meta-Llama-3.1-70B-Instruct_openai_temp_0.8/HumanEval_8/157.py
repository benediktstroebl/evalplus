```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    total_sum = sum(numbers)  # Calculate the sum of all numbers in the list
    product = 1  # Initialize the product to 1
    for num in numbers:  # Iterate over all numbers in the list
        product *= num  # Update the product by multiplying it with the current number
    return total_sum, product  # Return the sum and product as a tuple

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

However, the above implementation can be simplified using the `math.prod` function (Python 3.8+) to calculate the product of all numbers in the list:

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
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    total_sum = sum(numbers)  # Calculate the sum of all numbers in the list
    product = math.prod(numbers, start=1)  # Calculate the product of all numbers in the list
    return total_sum, product  # Return the sum and product as a tuple

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

In this version, `math.prod` is used with the `start` parameter set to 1 to handle the case where the input list is empty. If the input list is empty, `math.prod` will return the `start` value, which is 1 in this case.