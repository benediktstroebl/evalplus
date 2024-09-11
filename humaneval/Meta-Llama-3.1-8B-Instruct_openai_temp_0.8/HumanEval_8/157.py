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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Use the built-in sum function to calculate the sum of the list.
    # The sum function returns 0 for an empty list, as per the problem statement.
    total_sum = sum(numbers)

    # Use the built-in math.prod function to calculate the product of the list.
    # The math.prod function returns 1 for an empty list, as per the problem statement.
    import math
    total_product = math.prod(numbers)

    # Return the sum and product as a tuple.
    return total_sum, total_product


# Test the function with some examples.
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

Note that this script uses the built-in `sum` function to calculate the sum and the `math.prod` function to calculate the product of the list. If you're using a version of Python that doesn't support `math.prod`, you can use a list comprehension with the `*` operator to calculate the product:

```python
total_product = 1
for num in numbers:
    total_product *= num
```