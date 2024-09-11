```markdown
### Solution to Calculate Sum and Product of a List of Integers

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple consisting of their sum and product.

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple consisting of the sum and product of the input list.
    """

    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        
        # Multiply the current number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product


# Test the function with some examples
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([-1, 1, -2, 2]))  # (0, 4)
print(sum_product([5]))  # (5, 5)
print(sum_product([0]))  # (0, 0)
```

### Explanation

*   The function `sum_product` takes a list of integers `numbers` as input.
*   It initializes two variables, `total_sum` and `total_product`, to 0 and 1 respectively. These variables will be used to store the sum and product of the numbers in the list.
*   The function then iterates over each number in the list using a for loop.
*   Inside the loop, it adds the current number to `total_sum` and multiplies `total_product` by the current number.
*   After the loop finishes iterating over all numbers in the list, it returns a tuple consisting of `total_sum` and `total_product`.
*   The function is tested with some examples to demonstrate its correctness.