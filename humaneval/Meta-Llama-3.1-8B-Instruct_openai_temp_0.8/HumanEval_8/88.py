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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Use the built-in sum function to calculate the sum of the list
    # The sum function defaults to 0 if the list is empty
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the product of the list
    # The math.prod function defaults to 1 if the list is empty
    import math
    total_product = math.prod(numbers)
    
    # Return a tuple containing the sum and product
    return total_sum, total_product


# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script uses the built-in `sum` function and the `math.prod` function to calculate the sum and product of the list, respectively. The `math.prod` function is available in Python 3.8 and later versions. If you are using an earlier version of Python, you can use a list comprehension and the `*` operator to calculate the product:
```python
total_product = 1
for num in numbers:
    total_product *= num
```