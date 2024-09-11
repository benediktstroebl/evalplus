```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and the product of all integers in the input list.
    """
    total_sum = 0
    total_product = 1

    for num in numbers:
        total_sum += num
        total_product *= num

    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

In this script, we initialize the `total_sum` variable to 0 and the `total_product` variable to 1 to handle the edge case where the input list is empty. Then, we iterate through each number in the input list, adding it to `total_sum` and multiplying it to `total_product`. Finally, we return a tuple containing the calculated sum and product.

You can also use the built-in `sum()` and `math.prod()` functions (available in Python 3.8 and later) to make the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    return sum(numbers), math.prod(numbers, start=1)
```

In this version, `sum(numbers)` calculates the sum of all numbers in the list, and `math.prod(numbers, start=1)` calculates the product of all numbers in the list, with the `start` parameter set to 1 to handle the case where the input list is empty.