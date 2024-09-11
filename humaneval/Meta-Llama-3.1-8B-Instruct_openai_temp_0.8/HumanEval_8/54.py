```markdown
### Problem: Sum and Product of a List of Numbers

#### Solution

We will write a Python function `sum_product` that takes a list of integers as input and returns a tuple with the sum and product of all the integers in the list.

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
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test the function with an empty list
print(sum_product([]))  # Output: (0, 1)

# Test the function with a list of numbers
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
```

#### Explanation

The `sum_product` function uses a simple iterative approach to calculate the sum and product of a list of numbers. It initializes two variables `total_sum` and `total_product` to 0 and 1 respectively, which are then updated in each iteration of the loop. Finally, the function returns the calculated sum and product as a tuple.