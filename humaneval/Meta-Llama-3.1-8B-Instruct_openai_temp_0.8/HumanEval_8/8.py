Here's a Python function that meets the requirements:
```markdown
### Sum and Product of a List of Numbers

This script calculates the sum and product of all integers in a given list.

#### Code
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

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_of_numbers = 0
    product_of_numbers = 1

    # Iterate over the input list to calculate sum and product
    for number in numbers:
        sum_of_numbers += number
        product_of_numbers *= number

    return sum_of_numbers, product_of_numbers
```

#### Example Usage
```python
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
```